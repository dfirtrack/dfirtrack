from django import template
from git import Repo, GitCommandError
from os import getcwd

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v1.5.5'
    return versionnumber

@register.simple_tag
def dfirtrack_branch():
    repo = Repo(getcwd())
    try:
        return repo.active_branch
    except TypeError:               # coverage: ignore branch
        try:
            return repo.git.describe('--tags')
        except GitCommandError:
            return repo.git.describe('--all')
