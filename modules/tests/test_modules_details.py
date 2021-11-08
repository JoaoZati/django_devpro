import pytest
from django.urls import reverse
from model_mommy import mommy

from main.django_assertions import assert_contains
from modules.models import Lesson, Module


@pytest.fixture
def module(db):
    return mommy.make(Module)


@pytest.fixture
def lessons(module):
    return mommy.make(Lesson, 3, module=module)


@pytest.fixture
def resp(client, module, lessons):
    resp = client.get(reverse('modules:details', kwargs={'slug': module.slug}))
    return resp


def test_title(resp, module: Module):
    assert_contains(resp, module.title)


def test_description(resp, module: Module):
    assert_contains(resp, module.description)


def test_public(resp, module: Module):
    assert_contains(resp, module.public)


def test_lessons_titles(resp, lessons):
    for lesson in lessons:
        assert_contains(resp, lesson.title)


def test_lessons_links(resp, lessons):
    for lesson in lessons:
        assert_contains(resp, lesson.get_absolute_url())
