from django import template

register = template.Library()

@register.filter
def length_is(value, arg):
    """Return True if the length of the value is equal to arg."""
    return len(value) == arg
