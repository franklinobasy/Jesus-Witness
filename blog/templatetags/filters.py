from django import template

register = template.Library()


@register.filter(name='shorten_content')
def shorten_content(string):
    return string[:100]