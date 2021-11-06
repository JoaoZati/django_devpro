import pytest
from django.urls import reverse
from demonstration.models import Video
from main.django_assertions import assert_contains
from model_mommy import mommy


@pytest.fixture
def videos(db):
    return mommy.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('demonstration:index'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_videos(resp, videos):
    for video in videos:
        assert_contains(resp, video.title)


def test_link_videos(resp, videos):
    for video in videos:
        link_video = reverse('demonstration:video', args=(video.slug,))
        assert_contains(resp, f'href="{link_video}"')
