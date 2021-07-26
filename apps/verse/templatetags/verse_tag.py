from django import template

from apps.verse.models import Verse

register = template.Library()

#
# @register.simple_tag()
# def get_verses():
#     """Вывод всех стихов"""
#     return Verse.objects.all()

# @register.simple_tag()
# def get_verses():
#     """Вывод всех стихов"""
#     return Verse.objects.filter(recommend=True)