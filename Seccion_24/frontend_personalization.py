# ======= CONFIGURACIONES VISUALES Y PERSONALIZACIÓN ========
"""
Archivo de personalización visual para el sistema de gestión de biblioteca.
Contiene todos los estilos, colores, fuentes y configuraciones de diseño.
"""

# ======= CONFIGURACIÓN DE VENTANA PRINCIPAL ========
WINDOW_CONFIG = {
    'title': "📚 Gestión de Biblioteca - Sistema de Libros",
    'geometry': "900x650",
    'background': "#f0f0f0",
    'minsize': (850, 600)
}

# ======= CONFIGURACIÓN DE COLORES ========
COLORS = {
    # Colores principales
    'primary_bg': "#f0f0f0",
    'secondary_bg': "#ffffff", 
    'accent_bg': "#fafafa",
    
    # Colores de texto
    'primary_text': "#2c3e50",
    'secondary_text': "#7f8c8d",
    'success_text': "green",
    'error_text': "red",
    'warning_text': "orange",
    'info_text': "blue",
    
    # Colores de botones
    'btn_view': "#3498db",
    'btn_view_active': "#2980b9",
    'btn_search': "#9b59b6",
    'btn_search_active': "#8e44ad",
    'btn_add': "#27ae60",
    'btn_add_active': "#229954",
    'btn_update': "#f39c12",
    'btn_update_active': "#d68910",
    'btn_delete': "#e74c3c",
    'btn_delete_active': "#cb4335",
    'btn_clear': "#95a5a6",
    'btn_clear_active': "#85929e",
    'btn_exit': "#34495e",
    'btn_exit_active': "#2c3e50",
    
    # Colores de lista
    'list_bg': "#fafafa",
    'list_select_bg': "#3498db",
    'list_select_fg': "white",
    
    # Colores de scrollbar
    'scrollbar_bg': "#ecf0f1",
    
    # Colores de separadores
    'separator_color': "#bdc3c7"
}

# ======= CONFIGURACIÓN DE FUENTES ========
FONTS = {
    'title': ("Arial", 16, "bold"),
    'subtitle': ("Arial", 10),
    'section_header': ("Arial", 11, "bold"),
    'label': ("Arial", 10, "bold"),
    'entry': ("Arial", 10),
    'button': ("Arial", 10, "bold"),
    'list': ("Consolas", 9),
    'status': ("Arial", 9)
}

# ======= CONFIGURACIÓN DE DIMENSIONES ========
DIMENSIONS = {
    # Padding y espaciado
    'main_padx': 20,
    'main_pady': 15,
    'frame_padx': 15,
    'frame_pady': 10,
    'button_pady': 8,
    'button_padx': 5,
    
    # Tamaños de widgets
    'entry_width': 25,
    'button_width': 15,
    'button_height': 2,
    'list_height': 15,
    'list_width': 50,
    
    # Bordes
    'button_border': 2
}

# ======= CONFIGURACIÓN DE TEXTOS E ICONOS ========
TEXTS = {
    # Títulos principales
    'main_title': "📚 Sistema de Gestión de Biblioteca",
    'subtitle': "Administra tu colección de libros de manera sencilla",
    
    # Secciones
    'input_section': "Información del Libro",
    'list_section': "Lista de Libros",
    'actions_section': "Acciones",
    
    # Labels de campos
    'title_label': "Título:",
    'author_label': "Autor:",
    'year_label': "Año:",
    'isbn_label': "ISBN:",
    
    # Botones
    'btn_view': "Ver Todos",
    'btn_search': "Buscar",
    'btn_add': "Agregar",
    'btn_update': "Actualizar",
    'btn_delete': "Eliminar",
    'btn_clear': "Limpiar",
    'btn_exit': "Salir"
}

# ======= MENSAJES DEL SISTEMA ========
MESSAGES = {
    # Mensajes de éxito
    'book_added': "Libro agregado exitosamente",
    'book_updated': "Libro actualizado exitosamente", 
    'book_deleted': "Libro eliminado exitosamente",
    'fields_cleared': "Campos limpiados",
    'book_selected': "Libro seleccionado para editar",
    'app_started': "Aplicación iniciada correctamente",
    
    # Mensajes informativos
    'books_showing': "Mostrando {count} libros",
    'search_results': "Encontrados {count} resultados",
    'ready': "Listo para usar",
    
    # Mensajes de advertencia
    'title_required': "El título es obligatorio",
    'select_book': "Selecciona un libro de la lista",
    
    # Mensajes de confirmación
    'confirm_delete': "¿Estás seguro de que quieres eliminar este libro?",
    
    # Mensajes de error
    'error_loading': "Error al cargar libros: {error}",
    'error_search': "Error en la búsqueda: {error}",
    'error_adding': "Error al agregar libro: {error}",
    'error_updating': "Error al actualizar: {error}",
    'error_deleting': "Error al eliminar: {error}",
    'error_init': "Error al conectar con la base de datos: {error}",
    
    # Títulos de diálogos
    'dialog_error': "Error",
    'dialog_warning': "Advertencia",
    'dialog_confirm': "Confirmar",
    'dialog_init_error': "Error de Inicialización"
}

# ======= CONFIGURACIÓN DE ESTILOS DE WIDGETS ========
WIDGET_STYLES = {
    # Estilo para botones principales
    'button_main': {
        'width': DIMENSIONS['button_width'],
        'height': DIMENSIONS['button_height'],
        'font': FONTS['button'],
        'relief': 'raised',
        'bd': DIMENSIONS['button_border']
    },
    
    # Estilo para frames principales
    'frame_main': {
        'bg': COLORS['primary_bg'],
        'padx': DIMENSIONS['main_padx'],
        'pady': DIMENSIONS['main_pady']
    },
    
    # Estilo para frames de entrada
    'frame_input': {
        'bg': COLORS['secondary_bg'],
        'fg': COLORS['primary_text'],
        'padx': DIMENSIONS['frame_padx'],
        'pady': DIMENSIONS['frame_pady']
    },
    
    # Estilo para labels
    'label_main': {
        'font': FONTS['label'],
        'bg': COLORS['secondary_bg']
    },
    
    # Estilo para entries
    'entry_main': {
        'width': DIMENSIONS['entry_width'],
        'font': FONTS['entry']
    },
    
    # Estilo para listbox
    'listbox_main': {
        'height': DIMENSIONS['list_height'],
        'width': DIMENSIONS['list_width'],
        'font': FONTS['list'],
        'selectbackground': COLORS['list_select_bg'],
        'selectforeground': COLORS['list_select_fg'],
        'bg': COLORS['list_bg'],
        'fg': COLORS['primary_text']
    }
}

# ======= FUNCIÓN PARA APLICAR ESTILOS ========
def get_button_style(button_type):
    """Retorna el estilo específico para cada tipo de botón"""
    styles = {
        'view': {
            'bg': COLORS['btn_view'],
            'fg': 'white',
            'activebackground': COLORS['btn_view_active']
        },
        'search': {
            'bg': COLORS['btn_search'],
            'fg': 'white',
            'activebackground': COLORS['btn_search_active']
        },
        'add': {
            'bg': COLORS['btn_add'],
            'fg': 'white',
            'activebackground': COLORS['btn_add_active']
        },
        'update': {
            'bg': COLORS['btn_update'],
            'fg': 'white',
            'activebackground': COLORS['btn_update_active']
        },
        'delete': {
            'bg': COLORS['btn_delete'],
            'fg': 'white',
            'activebackground': COLORS['btn_delete_active']
        },
        'clear': {
            'bg': COLORS['btn_clear'],
            'fg': 'white',
            'activebackground': COLORS['btn_clear_active']
        },
        'exit': {
            'bg': COLORS['btn_exit'],
            'fg': 'white',
            'activebackground': COLORS['btn_exit_active']
        }
    }
    return {**WIDGET_STYLES['button_main'], **styles.get(button_type, {})}