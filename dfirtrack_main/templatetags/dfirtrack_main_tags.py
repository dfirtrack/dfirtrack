from django import template

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v1.7.3'
    return versionnumber
