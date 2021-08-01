from django import template

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v2.0.5'
    return versionnumber
