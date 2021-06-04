from django import template
from git import Repo, GitCommandError
from os import environ, getcwd

register = template.Library()

@register.simple_tag
def dfirtrack_version():
    versionnumber = 'v1.2.1'
    return versionnumber

@register.simple_tag
def dfirtrack_branch():
    repo = Repo(getcwd())
    try:
        return repo.active_branch
    except TypeError:
        try:
            return repo.git.describe('--tags')
        except GitCommandError:
            return repo.git.describe('--all')

@register.simple_tag
def github_ci():
    return 'CI' in environ
