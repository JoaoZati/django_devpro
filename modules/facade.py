from typing import List

from modules.models import Module, Lesson


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
    return Module.objects.order_by('order').all()
