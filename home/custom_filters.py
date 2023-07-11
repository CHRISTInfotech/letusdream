from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def read_more_link(text):
    return mark_safe(f"{text} <a href=''>Read More</a>")
