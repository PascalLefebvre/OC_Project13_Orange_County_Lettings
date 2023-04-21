"""The unit tests for the oc_lettings_site index view."""

from django.test import Client
from django.urls import reverse

import pytest


@pytest.fixture()
def http_response():
    client = Client()
    response = client.get(reverse("oc_lettings_site:index"))
    return response


def test_index_status_code(http_response):
    assert http_response.status_code == 200


def test_index_content(http_response):
    data = http_response.content.decode()
    assert "Welcome to Holiday Homes" in data


def test_index_profiles_index_url(http_response):
    data = http_response.content.decode()
    assert reverse("profiles:index") in data


def test_index_lettings_index_url(http_response):
    data = http_response.content.decode()
    assert reverse("lettings:index") in data
