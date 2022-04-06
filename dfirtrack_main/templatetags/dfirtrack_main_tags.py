from django import template

register = template.Library()


@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v2.4.6'
    return versionnumber


@register.simple_tag
def dep_bootstrap_version():
    return 'bootstrap-5.1.3'


@register.simple_tag
def dep_clipboard_version():
    return 'clipboard-2.0.10'


@register.simple_tag
def dep_datatables_version():
    return 'datatables-1.11.5'


@register.simple_tag
def dep_jquery_version():
    return 'jquery-3.6.0'


@register.simple_tag
def dep_swagger_ui_version():
    return 'swagger-ui-4.9.0'
