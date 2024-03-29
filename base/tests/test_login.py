import pytest
from django.urls import reverse
from model_mommy import mommy

from main.django_assertions import assert_contains, assert_not_contains


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


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_button_login_home(resp_home):
    assert_contains(resp_home, 'Login')


def test_link_login_home(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_home_logged_user(client_user_logged, db):
    return client_user_logged.get(reverse('base:home'))


def test_button_login_home_logged_user(resp_home_logged_user):
    assert_not_contains(resp_home_logged_user, 'Login')


def test_link_login_home_logged_user(resp_home_logged_user):
    assert_not_contains(resp_home_logged_user, reverse('login'))


def test_button_logout(resp_home_logged_user):
    assert_contains(resp_home_logged_user, reverse('logout'))


def test_username_logged_user(resp_home_logged_user, user_logged):
    assert_contains(resp_home_logged_user, user_logged.first_name)


def test_link_logout(resp_home_logged_user, user_logged):
    assert_contains(resp_home_logged_user, reverse('logout'))
