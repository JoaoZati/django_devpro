import pytest
from model_mommy import mommy
from django.urls import reverse
from demonstration.models import Video
from main.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('demonstration:video', args=(video.slug,)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_title_video(resp, video):
    assert_contains(resp, video.title)


def test_content_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}')


@pytest.fixture
def resp_video_not_found(client, video):
    print('resp')
    return client.get(reverse('demonstration:video', args=(video.slug+'random_content',)))


def test_status_code_video_not_found(resp_video_not_found):
    assert resp_video_not_found.status_code == 404
