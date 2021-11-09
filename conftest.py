import pytest
from model_mommy import mommy


@pytest.fixture
def user_logged(db, django_user_model):
    user_logged = mommy.make(django_user_model, first_name='Random')
    return user_logged


@pytest.fixture
def client_user_logged(user_logged, client):
    client.force_login(user_logged)
    return client
