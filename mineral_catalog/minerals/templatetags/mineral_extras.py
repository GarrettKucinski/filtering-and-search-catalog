from django import template

register = template.Library()


@register.filter
def replace_underscores_with_space(key):
    return ' '.join(key.split('_'))
