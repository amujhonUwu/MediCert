# utils.py

def days_to_text(days: int) -> str:
    """Convert a number of days into text (e.g., 3 -> THREE)."""
    numbers_map = {1: "UNO", 2: "DOS", 3: "TRES", 4: "CUATRO", 5: "CINCO", 6: "SEIS", 7:"SIETE"}
    return numbers_map.get(days, str(days).upper())

def translate_day(day: str) -> str:
    """Translate day names from English to Spanish."""
    days = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }
    return days.get(day, day)

def translate_month(month: str) -> str:
    """Translate month names from English to Spanish."""
    months = {
        'January': 'Enero',
        'February': 'Febrero',
        'March': 'Marzo',
        'April': 'Abril',
        'May': 'Mayo',
        'June': 'Junio',
        'July': 'Julio',
        'August': 'Agosto',
        'September': 'Septiembre',
        'October': 'Octubre',
        'November': 'Noviembre',
        'December': 'Diciembre'
    }
    return months.get(month, month)
