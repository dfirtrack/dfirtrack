from django import template

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v1.5.5'
    return versionnumber
