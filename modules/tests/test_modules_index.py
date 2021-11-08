import pytest
from django.urls import reverse
from model_mommy import mommy

from main.django_assertions import assert_contains # noqa
from modules.models import Lesson, Module


@pytest.fixture
def modules(db):
    return mommy.make(Module, 2)


@pytest.fixture
def lessons(modules):
    lessons = []
    for module in modules:
        lessons.extend(mommy.make(Lesson, 3, module=module))
    return lessons


@pytest.fixture
def resp(client, modules, lessons):
    resp = client.get(reverse('modules:index'))
    return resp


def test_modules_index(resp):
    assert resp.status_code == 200
