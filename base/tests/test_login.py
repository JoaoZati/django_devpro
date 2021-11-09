import pytest
from django.urls import reverse
from model_mommy import mommy


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def user(db, django_user_model):
    user_model = mommy.make(django_user_model)
    keyword = 'keyword'
    user_model.set_password(keyword)
    user_model.save()
    user_model.keyword_plane = keyword
    return user_model


@pytest.fixture
def resp_post(client, user):
    return client.post(reverse('login'), {'username': user.email, 'password': user.keyword_plane})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modules:index')
