from django import template

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v2.1.0'
    return versionnumber
