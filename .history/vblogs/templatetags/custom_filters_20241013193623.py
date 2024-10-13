# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def length_is(value, arg):
    return len(value) == arg
