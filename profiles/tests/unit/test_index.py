"""The unit tests for the profiles index view."""

from django.urls import reverse

import pytest


@pytest.fixture()
def http_response(db, client):
    response = client.get(reverse("profiles:index"))
    return response


def test_index_status_code(http_response):
    assert http_response.status_code == 200


def test_index_page_content_title(http_response):
    data = http_response.content.decode()
    assert "Profiles" in data


def test_index_page_content_profile_url(profile, http_response):
    data = http_response.content.decode()
    assert (
        reverse("profiles:profile", kwargs={"username": profile.user.username})
        in data
    )
