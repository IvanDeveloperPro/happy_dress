from django import template


register = template.Library()


@register.filter
def tranc_name(name):
    new_name = name.lower()[:4]
    return new_name
