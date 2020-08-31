from django import template
from git import Repo
from os import getcwd

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v0.3.8'
    return versionnumber

@register.simple_tag
def dfirtrack_branch():
    working_dir = getcwd()
    repo = Repo(working_dir)
    branch = repo.active_branch
    return branch
