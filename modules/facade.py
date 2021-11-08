from typing import List

from modules.models import Module


def list_modules_ordered() -> List[Module]:
    """
    List of modules ordered by titles
    :return:
    """

    return list(Module.objects.order_by('order').all())


def find_module(slug):
    return Module.objects.get(slug=slug)
