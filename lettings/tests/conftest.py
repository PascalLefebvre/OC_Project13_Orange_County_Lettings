import pytest

from lettings.models import Address, Letting


@pytest.fixture()
def letting(db):
    address = Address.objects.create(
        number="2016",
        street="Avenue da India, Belem",
        city="Lisboa",
        state="Lisboa",
        zip_code="12345",
        country_iso_code="789",
    )
    letting = Letting.objects.create(
        title="Magnificent view on the Tage",
        address=address,
    )
    return letting
