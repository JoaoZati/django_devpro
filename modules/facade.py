from typing import List

from modules.models import Module, Lesson

from django.db.models import Prefetch


def list_modules_ordered() -> List[Module]:
    """
    List of modules ordered by titles
    :return:
    """

    return list(Module.objects.order_by('order').all())


def find_module(slug):
    return Module.objects.get(slug=slug)


def list_modules_ordered_lessons(module: Module):
    return list(module.lesson_set.order_by('order').all())


def find_lesson(slug):
    return Lesson.objects.select_related('module').get(slug=slug)


def list_modules_and_lessons():
    ordered_lessons = Lesson.objects.order_by('order')
    return Module.objects.order_by('order').prefetch_related(
        Prefetch('lesson_set', queryset=ordered_lessons, to_attr='lessons')
    ).all()
