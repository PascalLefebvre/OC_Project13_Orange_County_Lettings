"""The unit tests for the profile view."""

from django.urls import reverse

import pytest


@pytest.fixture()
def http_response(db, profile, client):
    response = client.get(
        reverse("profiles:profile", kwargs={"username": profile.user.username})
    )
    return response


def test_profile_status_code(http_response):
    assert http_response.status_code == 200


def test_profile_page_content_username(profile, http_response):
    data = http_response.content.decode()
    assert profile.user.username in data


def test_profile_page_content_favorite_city(profile, http_response):
    data = http_response.content.decode()
    assert profile.favorite_city in data
