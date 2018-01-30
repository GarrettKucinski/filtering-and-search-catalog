from django import template
from random import randint
from minerals.models import Mineral

register = template.Library()


@register.filter
def replace_underscores_with_space(key):
    return ' '.join(key.split('_'))


@register.simple_tag
def generate_random_num():
    mineral_count = Mineral.objects.all().count()
    return randint(1, mineral_count)
