# ======= SISTEMA DE VALIDACIONES ========
"""
Archivo de validaciones para el sistema de gestión de biblioteca.
Contiene todas las funciones de validación de datos y mensajes de error específicos.
"""

import re
from datetime import datetime

# ======= CONFIGURACIÓN DE VALIDACIONES ========
VALIDATION_RULES = {
    'title': {
        'min_length': 1,
        'max_length': 200,
        'required': True,
        'strip_whitespace': True
    },
    'author': {
        'min_length': 0,
        'max_length': 150,
        'required': False,
        'strip_whitespace': True,
        'allow_special_chars': True
    },
    'year': {
        'min_value': 1000,
        'max_value': datetime.now().year + 5,  # Permitir algunos años futuros
        'required': False,
        'allow_empty': True
    },
    'isbn': {
        'required': False,
        'allow_empty': True,
        'formats': ['isbn10', 'isbn13', 'simple_number']
    }
}

# ======= MENSAJES DE VALIDACIÓN ========
VALIDATION_MESSAGES = {
    'title_required': "❌ El título es obligatorio",
    'title_too_long': "❌ El título no puede exceder {max_length} caracteres",
    'title_too_short': "❌ El título debe tener al menos {min_length} carácter",
    
    'author_too_long': "❌ El nombre del autor no puede exceder {max_length} caracteres",
    'author_invalid_chars': "❌ El nombre del autor contiene caracteres no válidos",
    
    'year_invalid': "❌ El año debe ser un número válido",
    'year_too_old': "❌ El año debe ser mayor a {min_value}",
    'year_too_future': "❌ El año no puede ser mayor a {max_value}",
    
    'isbn_invalid': "❌ El ISBN debe tener 10 o 13 dígitos, o ser un número válido",
    'isbn_format_error': "❌ Formato de ISBN incorrecto. Use solo números (ej: 9780743273565)",
    
    'validation_success': "✅ Todos los datos son válidos",
    'multiple_errors': "❌ Se encontraron {count} errores de validación"
}

# ======= CLASE DE RESULTADOS DE VALIDACIÓN ========
class ValidationResult:
    """Clase para manejar los resultados de validación"""
    
    def __init__(self):
        self.is_valid = True
        self.errors = []
        self.warnings = []
        self.sanitized_data = {}
    
    def add_error(self, field, message):
        """Agregar un error de validación"""
        self.is_valid = False
        self.errors.append({'field': field, 'message': message})
    
    def add_warning(self, field, message):
        """Agregar una advertencia"""
        self.warnings.append({'field': field, 'message': message})
    
    def get_error_messages(self):
        """Obtener lista de mensajes de error"""
        return [error['message'] for error in self.errors]
    
    def get_warning_messages(self):
        """Obtener lista de mensajes de advertencia"""
        return [warning['message'] for warning in self.warnings]
    
    def get_formatted_errors(self):
        """Obtener errores formateados para mostrar"""
        if not self.errors:
            return ""
        
        if len(self.errors) == 1:
            return self.errors[0]['message']
        
        error_list = "\n".join([f"• {error['message']}" for error in self.errors])
        header = VALIDATION_MESSAGES['multiple_errors'].format(count=len(self.errors))
        return f"{header}\n\n{error_list}"

# ======= FUNCIONES DE VALIDACIÓN ESPECÍFICAS ========
def validate_title(title):
    """Validar el título del libro"""
    errors = []
    rules = VALIDATION_RULES['title']
    
    # Limpiar espacios en blanco
    if rules['strip_whitespace']:
        title = title.strip()
    
    # Verificar si es requerido
    if rules['required'] and not title:
        errors.append(VALIDATION_MESSAGES['title_required'])
        return errors, title
    
    # Verificar longitud mínima
    if title and len(title) < rules['min_length']:
        errors.append(VALIDATION_MESSAGES['title_too_short'].format(min_length=rules['min_length']))
    
    # Verificar longitud máxima
    if title and len(title) > rules['max_length']:
        errors.append(VALIDATION_MESSAGES['title_too_long'].format(max_length=rules['max_length']))
    
    return errors, title

def validate_author(author):
    """Validar el nombre del autor"""
    errors = []
    warnings = []
    rules = VALIDATION_RULES['author']
    
    # Limpiar espacios en blanco
    if rules['strip_whitespace']:
        author = author.strip()
    
    # Si está vacío y no es requerido, está bien
    if not author and not rules['required']:
        return errors, warnings, author
    
    # Verificar longitud máxima
    if author and len(author) > rules['max_length']:
        errors.append(VALIDATION_MESSAGES['author_too_long'].format(max_length=rules['max_length']))
    
    # Validar caracteres (permitir letras, espacios, puntos, guiones, apostrofes)
    if author and not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\.\-\']+$", author):
        errors.append(VALIDATION_MESSAGES['author_invalid_chars'])
    
    # Advertencia si está vacío
    if not author:
        warnings.append("⚠️ Se recomienda especificar el autor")
    
    return errors, warnings, author

def validate_year(year_str):
    """Validar el año de publicación"""
    errors = []
    warnings = []
    rules = VALIDATION_RULES['year']
    
    # Limpiar espacios
    year_str = str(year_str).strip()
    
    # Si está vacío y se permite, está bien
    if not year_str and rules['allow_empty']:
        warnings.append("⚠️ Se recomienda especificar el año de publicación")
        return errors, warnings, ""
    
    # Intentar convertir a entero
    try:
        year = int(year_str)
    except ValueError:
        errors.append(VALIDATION_MESSAGES['year_invalid'])
        return errors, warnings, year_str
    
    # Verificar rango mínimo
    if year < rules['min_value']:
        errors.append(VALIDATION_MESSAGES['year_too_old'].format(min_value=rules['min_value']))
    
    # Verificar rango máximo
    if year > rules['max_value']:
        errors.append(VALIDATION_MESSAGES['year_too_future'].format(max_value=rules['max_value']))
    
    # Advertencia para años muy antiguos o futuros
    current_year = datetime.now().year
    if year < 1800:
        warnings.append("⚠️ Año muy antiguo, verifique que sea correcto")
    elif year > current_year:
        warnings.append("⚠️ Año futuro detectado")
    
    return errors, warnings, str(year)

def validate_isbn(isbn_str):
    """Validar el ISBN"""
    errors = []
    warnings = []
    rules = VALIDATION_RULES['isbn']
    
    # Limpiar espacios y guiones
    isbn_str = str(isbn_str).strip().replace('-', '').replace(' ', '')
    
    # Si está vacío y se permite, está bien
    if not isbn_str and rules['allow_empty']:
        warnings.append("⚠️ Se recomienda especificar el ISBN")
        return errors, warnings, ""
    
    # Si no está vacío, validar formato
    if isbn_str:
        # Verificar que solo contenga dígitos
        if not isbn_str.isdigit():
            errors.append(VALIDATION_MESSAGES['isbn_format_error'])
            return errors, warnings, isbn_str
        
        # Verificar longitud (ISBN-10: 10 dígitos, ISBN-13: 13 dígitos, o número simple)
        length = len(isbn_str)
        if length not in [10, 13] and length < 6:
            errors.append(VALIDATION_MESSAGES['isbn_invalid'])
        elif length == 10:
            warnings.append("ℹ️ ISBN-10 detectado")
        elif length == 13:
            warnings.append("ℹ️ ISBN-13 detectado")
        elif length > 13:
            warnings.append("⚠️ ISBN más largo de lo normal")
    
    return errors, warnings, isbn_str

# ======= FUNCIÓN PRINCIPAL DE VALIDACIÓN ========
def validate_book_data(title, author, year, isbn):
    """Validar todos los datos de un libro"""
    result = ValidationResult()
    
    # Validar título
    title_errors, clean_title = validate_title(title)
    for error in title_errors:
        result.add_error('title', error)
    result.sanitized_data['title'] = clean_title
    
    # Validar autor
    author_errors, author_warnings, clean_author = validate_author(author)
    for error in author_errors:
        result.add_error('author', error)
    for warning in author_warnings:
        result.add_warning('author', warning)
    result.sanitized_data['author'] = clean_author
    
    # Validar año
    year_errors, year_warnings, clean_year = validate_year(year)
    for error in year_errors:
        result.add_error('year', error)
    for warning in year_warnings:
        result.add_warning('year', warning)
    result.sanitized_data['year'] = clean_year
    
    # Validar ISBN
    isbn_errors, isbn_warnings, clean_isbn = validate_isbn(isbn)
    for error in isbn_errors:
        result.add_error('isbn', error)
    for warning in isbn_warnings:
        result.add_warning('isbn', warning)
    result.sanitized_data['isbn'] = clean_isbn
    
    return result

# ======= FUNCIONES DE VALIDACIÓN PARA BÚSQUEDA ========
def validate_search_data(title, author, year, isbn):
    """Validar datos para búsqueda (más permisivo)"""
    result = ValidationResult()
    
    # Para búsqueda, todos los campos son opcionales
    # Solo validar formato básico si no están vacíos
    
    if title:
        if len(title) > 200:
            result.add_warning('title', "⚠️ Búsqueda de título muy larga")
        result.sanitized_data['title'] = title.strip()
    else:
        result.sanitized_data['title'] = ""
    
    if author:
        if len(author) > 150:
            result.add_warning('author', "⚠️ Búsqueda de autor muy larga")
        result.sanitized_data['author'] = author.strip()
    else:
        result.sanitized_data['author'] = ""
    
    if year:
        try:
            int(year)
            result.sanitized_data['year'] = year.strip()
        except ValueError:
            result.add_warning('year', "⚠️ Año para búsqueda debe ser numérico")
            result.sanitized_data['year'] = ""
    else:
        result.sanitized_data['year'] = ""
    
    if isbn:
        # Para búsqueda, permitir cualquier formato de ISBN
        clean_isbn = isbn.strip().replace('-', '').replace(' ', '')
        result.sanitized_data['isbn'] = clean_isbn
    else:
        result.sanitized_data['isbn'] = ""
    
    return result

# ======= FUNCIÓN DE AYUDA ========
def get_validation_help():
    """Obtener ayuda sobre las reglas de validación"""
    help_text = """
📋 REGLAS DE VALIDACIÓN:

📖 Título:
   • Obligatorio
   • Máximo 200 caracteres
   • Se eliminan espacios al inicio y final

👤 Autor:
   • Opcional pero recomendado
   • Máximo 150 caracteres
   • Solo letras, espacios, puntos, guiones y apostrofes

📅 Año:
   • Opcional
   • Número entre 1000 y {max_year}
   • Se recomienda especificar

🔢 ISBN:
   • Opcional
   • 10 o 13 dígitos (sin guiones ni espacios)
   • También acepta números simples
   
✅ Todos los campos se limpian automáticamente
⚠️  Las advertencias no impiden guardar el libro
    """.format(max_year=datetime.now().year + 5)
    
    return help_text