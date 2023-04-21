"""The unit tests for the lettings index view."""

from django.urls import reverse

import pytest


@pytest.fixture()
def http_response(db, client):
    response = client.get(reverse("lettings:index"))
    return response


def test_index_status_code(http_response):
    assert http_response.status_code == 200


def test_index_page_content_title(http_response):
    data = http_response.content.decode()
    assert "Lettings" in data


def test_index_page_content_letting_url(letting, http_response):
    data = http_response.content.decode()
    assert (
        reverse("lettings:letting", kwargs={"letting_id": letting.id}) in data
    )
