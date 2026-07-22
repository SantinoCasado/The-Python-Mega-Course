from tkinter import *
from tkinter import ttk, messagebox
import backend
from frontend_personalization import *
from validation import validate_book_data, validate_search_data, get_validation_help

# Variable para mantener los datos originales (sin formatear)
original_data = []

# ======= FUNCIONES DE LÓGICA DE NEGOCIO ========
def view_command():
    """Mostrar todos los libros"""
    global original_data
    list1.delete(0, END)
    try:
        original_data = backend.view_raw()
        formatted_data = backend.view()
        for row in formatted_data:
            list1.insert(END, row)
        status_label.config(text=MESSAGES['books_showing'].format(count=len(formatted_data)), 
                          fg=COLORS['success_text'])
    except Exception as e:
        messagebox.showerror(MESSAGES['dialog_error'], 
                           MESSAGES['error_loading'].format(error=str(e)))

def search_command():
    """Buscar libros con validación"""
    global original_data
    list1.delete(0, END)
    
    # Validar datos de búsqueda (más permisivo)
    validation_result = validate_search_data(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get()
    )
    
    # Mostrar advertencias si las hay
    if validation_result.warnings:
        warning_msg = "\n".join(validation_result.get_warning_messages())
        messagebox.showinfo("Información", warning_msg)
    
    try:
        # Usar datos sanitizados para la búsqueda
        data = validation_result.sanitized_data
        original_data = backend.search_raw(data['title'], data['author'], data['year'], data['isbn'])
        formatted_data = backend.search(data['title'], data['author'], data['year'], data['isbn'])
        for row in formatted_data:
            list1.insert(END, row)
        status_label.config(text=MESSAGES['search_results'].format(count=len(formatted_data)), 
                          fg=COLORS['info_text'])
    except Exception as e:
        messagebox.showerror(MESSAGES['dialog_error'], 
                           MESSAGES['error_search'].format(error=str(e)))

def add_command():
    """Agregar nuevo libro con validación"""
    # Validar todos los datos
    validation_result = validate_book_data(
        title_text.get(), author_text.get(), year_text.get(), isbn_text.get()
    )
    
    # Si hay errores, mostrarlos
    if not validation_result.is_valid:
        messagebox.showerror(MESSAGES['dialog_error'], validation_result.get_formatted_errors())
        return
    
    # Mostrar advertencias si las hay
    if validation_result.warnings:
        warning_msg = "\n".join(validation_result.get_warning_messages())
        if not messagebox.askyesno("Advertencias", f"{warning_msg}\n\n¿Continuar agregando el libro?"):
            return
    
    try:
        # Usar datos sanitizados
        data = validation_result.sanitized_data
        backend.insert(data['title'], data['author'], data['year'], data['isbn'])
        clear_entries()
        view_command()
        status_label.config(text=MESSAGES['book_added'], fg=COLORS['success_text'])
    except Exception as e:
        messagebox.showerror(MESSAGES['dialog_error'], 
                           MESSAGES['error_adding'].format(error=str(e)))

def update_command():
    """Actualizar libro seleccionado con validación"""
    try:
        selected_index = list1.curselection()[0]
        selected_tuple = original_data[selected_index]
        
        # Validar todos los datos
        validation_result = validate_book_data(
            title_text.get(), author_text.get(), year_text.get(), isbn_text.get()
        )
        
        # Si hay errores, mostrarlos
        if not validation_result.is_valid:
            messagebox.showerror(MESSAGES['dialog_error'], validation_result.get_formatted_errors())
            return
        
        # Mostrar advertencias si las hay
        if validation_result.warnings:
            warning_msg = "\n".join(validation_result.get_warning_messages())
            if not messagebox.askyesno("Advertencias", f"{warning_msg}\n\n¿Continuar actualizando el libro?"):
                return
        
        # Usar datos sanitizados
        data = validation_result.sanitized_data
        backend.update(selected_tuple[0], data['title'], data['author'], data['year'], data['isbn'])
        view_command()
        status_label.config(text=MESSAGES['book_updated'], fg=COLORS['success_text'])
    except IndexError:
        messagebox.showwarning(MESSAGES['dialog_warning'], MESSAGES['select_book'])
    except Exception as e:
        messagebox.showerror(MESSAGES['dialog_error'], 
                           MESSAGES['error_updating'].format(error=str(e)))

def delete_command():
    """Eliminar libro seleccionado"""
    try:
        selected_index = list1.curselection()[0]
        selected_tuple = original_data[selected_index]
        
        # Confirmación antes de eliminar
        if messagebox.askyesno(MESSAGES['dialog_confirm'], MESSAGES['confirm_delete']):
            backend.delete(selected_tuple[0])
            view_command()
            clear_entries()
            status_label.config(text=MESSAGES['book_deleted'], fg=COLORS['warning_text'])
    except IndexError:
        messagebox.showwarning(MESSAGES['dialog_warning'], MESSAGES['select_book'])
    except Exception as e:
        messagebox.showerror(MESSAGES['dialog_error'], 
                           MESSAGES['error_deleting'].format(error=str(e)))

def get_selected_row(event):
    """Cargar datos del libro seleccionado en los campos de entrada"""
    try:
        selected_index = list1.curselection()[0]
        selected_tuple = original_data[selected_index]
        
        # Limpiar campos
        clear_entries()
        
        # Insertar valores seleccionados
        e1.insert(0, selected_tuple[1])  # title
        e2.insert(0, selected_tuple[2])  # author
        e3.insert(0, str(selected_tuple[3]))  # year
        e4.insert(0, str(selected_tuple[4]))  # isbn
        
        status_label.config(text=MESSAGES['book_selected'], fg=COLORS['info_text'])
    except IndexError:
        pass

def clear_entries():
    """Limpiar todos los campos de entrada"""
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    status_label.config(text=MESSAGES['fields_cleared'], fg=COLORS['secondary_text'])

def show_validation_help():
    """Mostrar ayuda sobre las reglas de validación"""
    help_text = get_validation_help()
    messagebox.showinfo("📋 Ayuda de Validación", help_text)

def validate_entry_realtime(field_name, value):
    """Validación en tiempo real de campos"""
    if field_name == 'title' and len(value) > 200:
        status_label.config(text="⚠️ Título muy largo (máx. 200 caracteres)", fg=COLORS['warning_text'])
    elif field_name == 'author' and len(value) > 150:
        status_label.config(text="⚠️ Autor muy largo (máx. 150 caracteres)", fg=COLORS['warning_text'])
    elif field_name == 'year' and value:
        try:
            year = int(value)
            if year < 1000 or year > 2030:
                status_label.config(text="⚠️ Año fuera de rango (1000-2030)", fg=COLORS['warning_text'])
            else:
                status_label.config(text="✅ Año válido", fg=COLORS['success_text'])
        except ValueError:
            if value:
                status_label.config(text="⚠️ El año debe ser numérico", fg=COLORS['warning_text'])
    elif field_name == 'isbn' and value and not value.isdigit():
        status_label.config(text="⚠️ ISBN debe contener solo números", fg=COLORS['warning_text'])

def on_title_change(*args):
    """Callback para validación en tiempo real del título"""
    validate_entry_realtime('title', title_text.get())

def on_author_change(*args):
    """Callback para validación en tiempo real del autor"""
    validate_entry_realtime('author', author_text.get())

def on_year_change(*args):
    """Callback para validación en tiempo real del año"""
    validate_entry_realtime('year', year_text.get())

def on_isbn_change(*args):
    """Callback para validación en tiempo real del ISBN"""
    validate_entry_realtime('isbn', isbn_text.get())

# ======= CONSTRUCCIÓN DE LA INTERFAZ ========
def create_interface():
    """Función principal para crear toda la interfaz"""
    global window, main_frame, list1, status_label
    global title_text, author_text, year_text, isbn_text
    global e1, e2, e3, e4
    
    # ======= Crear ventana principal ========
    window = Tk()
    window.title(WINDOW_CONFIG['title'])
    window.geometry(WINDOW_CONFIG['geometry'])
    window.configure(bg=WINDOW_CONFIG['background'])
    window.minsize(*WINDOW_CONFIG['minsize'])
    
    # ======= Frame principal con padding ========
    main_frame = Frame(window, **WIDGET_STYLES['frame_main'])
    main_frame.pack(fill=BOTH, expand=True)
    
    create_header()
    create_input_section()
    create_main_content()
    create_status_bar()
    
    return window

def create_header():
    """Crear la sección de encabezado"""
    title_frame = Frame(main_frame, bg=COLORS['primary_bg'])
    title_frame.pack(fill=X, pady=(0, 20))
    
    title_label = Label(title_frame, text=TEXTS['main_title'], 
                       font=FONTS['title'], bg=COLORS['primary_bg'], fg=COLORS['primary_text'])
    title_label.pack()
    
    subtitle_label = Label(title_frame, text=TEXTS['subtitle'], 
                          font=FONTS['subtitle'], bg=COLORS['primary_bg'], fg=COLORS['secondary_text'])
    subtitle_label.pack()

def create_input_section():
    """Crear la sección de entrada de datos"""
    global title_text, author_text, year_text, isbn_text
    global e1, e2, e3, e4
    
    input_frame = LabelFrame(main_frame, text=TEXTS['input_section'], 
                            font=FONTS['section_header'], **WIDGET_STYLES['frame_input'])
    input_frame.pack(fill=X, pady=(0, 15))
    
    # Primera fila
    Label(input_frame, text=TEXTS['title_label'], **WIDGET_STYLES['label_main']).grid(
        row=0, column=0, sticky=W, padx=(0, 10), pady=5)
    title_text = StringVar()
    title_text.trace('w', on_title_change)  # Validación en tiempo real
    e1 = Entry(input_frame, textvariable=title_text, **WIDGET_STYLES['entry_main'])
    e1.grid(row=0, column=1, padx=(0, 20), pady=5, sticky=W)
    
    Label(input_frame, text=TEXTS['author_label'], **WIDGET_STYLES['label_main']).grid(
        row=0, column=2, sticky=W, padx=(0, 10), pady=5)
    author_text = StringVar()
    author_text.trace('w', on_author_change)  # Validación en tiempo real
    e2 = Entry(input_frame, textvariable=author_text, **WIDGET_STYLES['entry_main'])
    e2.grid(row=0, column=3, pady=5, sticky=W)
    
    # Segunda fila
    Label(input_frame, text=TEXTS['year_label'], **WIDGET_STYLES['label_main']).grid(
        row=1, column=0, sticky=W, padx=(0, 10), pady=5)
    year_text = StringVar()
    year_text.trace('w', on_year_change)  # Validación en tiempo real
    e3 = Entry(input_frame, textvariable=year_text, **WIDGET_STYLES['entry_main'])
    e3.grid(row=1, column=1, padx=(0, 20), pady=5, sticky=W)
    
    Label(input_frame, text=TEXTS['isbn_label'], **WIDGET_STYLES['label_main']).grid(
        row=1, column=2, sticky=W, padx=(0, 10), pady=5)
    isbn_text = StringVar()
    isbn_text.trace('w', on_isbn_change)  # Validación en tiempo real
    e4 = Entry(input_frame, textvariable=isbn_text, **WIDGET_STYLES['entry_main'])
    e4.grid(row=1, column=3, pady=5, sticky=W)

def create_main_content():
    """Crear el contenido principal (lista y botones)"""
    global list1
    
    content_frame = Frame(main_frame, bg=COLORS['primary_bg'])
    content_frame.pack(fill=BOTH, expand=True)
    
    create_list_section(content_frame)
    create_buttons_section(content_frame)

def create_list_section(parent):
    """Crear la sección de la lista"""
    global list1
    
    list_frame = LabelFrame(parent, text=TEXTS['list_section'], 
                           font=FONTS['section_header'], **WIDGET_STYLES['frame_input'])
    list_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 15))
    
    list_container = Frame(list_frame, bg=COLORS['secondary_bg'])
    list_container.pack(fill=BOTH, expand=True)
    
    list1 = Listbox(list_container, **WIDGET_STYLES['listbox_main'])
    list1.pack(side=LEFT, fill=BOTH, expand=True)
    
    sb1 = Scrollbar(list_container, bg=COLORS['scrollbar_bg'])
    sb1.pack(side=RIGHT, fill=Y)
    
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)
    list1.bind('<<ListboxSelect>>', get_selected_row)

def create_buttons_section(parent):
    """Crear la sección de botones"""
    button_frame = LabelFrame(parent, text=TEXTS['actions_section'], 
                             font=FONTS['section_header'], **WIDGET_STYLES['frame_input'])
    button_frame.pack(side=RIGHT, fill=BOTH, padx=(10, 0))  # Cambié fill=Y por fill=BOTH y agregué padding
    
    # Crear todos los botones
    buttons = [
        (TEXTS['btn_view'], view_command, 'view'),
        (TEXTS['btn_search'], search_command, 'search'),
        (TEXTS['btn_add'], add_command, 'add'),
        (TEXTS['btn_update'], update_command, 'update'),
        (TEXTS['btn_delete'], delete_command, 'delete'),
        (None, None, None),  # Separador
        (TEXTS['btn_clear'], clear_entries, 'clear'),
        ("📋 Ayuda", show_validation_help, 'search'),  # Botón de ayuda
        (TEXTS['btn_exit'], lambda: window.quit(), 'exit')
    ]
    
    for text, command, style_type in buttons:
        if text is None:  # Separador
            separator = Frame(button_frame, height=2, bg=COLORS['separator_color'])
            separator.pack(fill=X, pady=10)  # Reduje el padding del separador
        else:
            btn = Button(button_frame, text=text, command=command, 
                        **get_button_style(style_type))
            btn.pack(pady=5, padx=DIMENSIONS['button_padx'])  # Reduje el padding vertical

def create_status_bar():
    """Crear la barra de estado"""
    global status_label
    
    status_frame = Frame(main_frame, bg=COLORS['primary_bg'])
    status_frame.pack(fill=X, pady=(15, 0))
    
    status_label = Label(status_frame, text=MESSAGES['ready'], 
                        font=FONTS['status'], bg=COLORS['primary_bg'], fg=COLORS['secondary_text'])
    status_label.pack(side=LEFT)

def initialize_app():
    """Inicializar la aplicación"""
    try:
        backend.connect()
        view_command()
        status_label.config(text=MESSAGES['app_started'], fg=COLORS['success_text'])
    except Exception as e:
        messagebox.showerror(MESSAGES['dialog_init_error'], 
                           MESSAGES['error_init'].format(error=str(e)))
    
    # Foco inicial en el campo de título
    e1.focus()

# ======= FUNCIÓN PRINCIPAL ========
def main():
    """Función principal para ejecutar la aplicación"""
    create_interface()
    initialize_app()
    window.mainloop()

# ======= EJECUCIÓN ========
if __name__ == "__main__":
    main()