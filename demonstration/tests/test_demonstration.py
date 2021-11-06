import pytest
from django.urls import reverse

from main.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('demonstration:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Demonstration Video: Motivation</h1>')


def test_content_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/600572543"')
