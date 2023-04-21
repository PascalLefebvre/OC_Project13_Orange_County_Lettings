"""The unit tests for the letting view."""

from django.urls import reverse

import pytest


@pytest.fixture()
def http_response(db, letting, client):
    response = client.get(
        reverse("lettings:letting", kwargs={"letting_id": letting.id})
    )
    return response


def test_letting_status_code(http_response):
    assert http_response.status_code == 200


def test_letting_page_content_title(letting, http_response):
    data = http_response.content.decode()
    assert letting.title in data


def test_letting_page_content_address_street(letting, http_response):
    data = http_response.content.decode()
    assert letting.address.street in data
