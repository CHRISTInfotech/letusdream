from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def read_more_link(text):
    return mark_safe(f"{text} <a href=''>Read More</a>")

@register.filter
def multiply(value, arg):
    """Multiply the value by the argument."""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def gradient_class(counter):
    """Calculate gradient class number (1-6) based on counter."""
    try:
        return ((int(counter) + 6) % 6) + 1
    except (ValueError, TypeError):
        return 1
