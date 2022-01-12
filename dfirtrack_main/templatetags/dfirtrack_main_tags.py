from django import template

register = template.Library()


@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v2.3.1'
    return versionnumber
