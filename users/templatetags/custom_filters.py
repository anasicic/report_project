from django import template
import locale

register = template.Library()

@register.filter
def format_number(value):
    try:
        locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8') 
        formatted_value = locale.format_string("%0.2f", value, grouping=True)
        return formatted_value
    except (ValueError, locale.Error):
        return value 