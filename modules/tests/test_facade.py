import pytest
from model_mommy import mommy

from modules import facade
from modules.models import Module


@pytest.fixture
def modules(db):
    return [mommy.make(Module, title=s) for s in 'title1 title2'.split()]


def test_list_modules_ordered(modules):
    assert list(sorted(modules, key=lambda module: module.title)) == facade.list_modules_ordered()
