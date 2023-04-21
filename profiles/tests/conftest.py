import pytest

from profiles.models import Profile


@pytest.fixture()
def profile(db, django_user_model):
    user = django_user_model.objects.create(
        username="testuser", password="Abc1234!"
    )
    profile = Profile.objects.create(user=user, favorite_city="Lisbonne")
    return profile
