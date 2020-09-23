from django import template
from git import Repo
from os import environ, getcwd

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v0.4.0'
    return versionnumber

@register.simple_tag
def github_ci():
    if "CI" in environ:
        ci = False
    else:
        ci = True
    return ci

if not "CI" in environ:
    @register.simple_tag
    def dfirtrack_branch():
        working_dir = getcwd()
        repo = Repo(working_dir)
        branch = repo.active_branch
        return branch
else:
    @register.simple_tag
    def dfirtrack_branch():
        return "unknown"