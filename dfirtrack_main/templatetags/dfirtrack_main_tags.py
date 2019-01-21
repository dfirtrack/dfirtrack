from django import template

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v0.1.14'
    return versionnumber
