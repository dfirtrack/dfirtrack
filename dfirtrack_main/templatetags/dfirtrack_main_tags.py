from django import template

register = template.Library()


@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v2.4.6'
    return versionnumber
