from django import template

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v2.0.0'
    return versionnumber
