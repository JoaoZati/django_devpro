import pytest
from django.urls import reverse
from model_mommy import mommy

from main.django_assertions import assert_contains
from modules.models import Lesson, Module


@pytest.fixture
def module(db):
    return mommy.make(Module)


@pytest.fixture
def lesson(module):
    return mommy.make(Lesson, module=module)


@pytest.fixture
def resp(client_user_logged, lesson):
    resp = client_user_logged.get(reverse('modules:lesson', kwargs={'slug': lesson.slug}))
    return resp


def test_title(resp, lesson):
    assert_contains(resp, lesson.title)


def test_vimeo(resp, lesson):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ lesson.vimeo_id }"')


def test_modulo_breadcrumb(resp, module):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{module.get_absolute_url()}">{module.title}</a></li>')


@pytest.fixture
def resp_not_logged(client, lesson):
    resp = client.get(reverse('modules:lesson', kwargs={'slug': lesson.slug}))
    return resp


def test_user_not_logged(resp_not_logged):
    assert resp_not_logged.status_code == 302
    assert resp_not_logged.url.startswith(reverse('login'))
