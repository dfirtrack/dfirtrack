from django import template

register = template.Library()


@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v2.4.3'
    return versionnumber
