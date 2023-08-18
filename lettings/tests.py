import pytest
from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from lettings.models import Letting, Address


@pytest.fixture
def address():
    address = Address.objects.create(
        number=34,
        street="Rue anatole france",
        city="venissieux",
        state="france",
        zip_code=69200,
        country_iso_code="FR",
    )
    return address


@pytest.fixture
def letting(address):
    letting = Letting.objects.create(title="boulangerie du parc", address=address)
    return letting


class TestLettingsViews:
    def test_index_view(self):
        client = Client()
        path = reverse("index")
        response = client.get(path)
        content = response.content.decode()
        expected_content = 'Welcome to Holiday Homes'

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")

    @pytest.mark.django_db
    def test_lettings_index_view(self):
        client = Client()
        path = reverse("lettings_index")
        response = client.get(path)
        content = response.content.decode()
        expected_content = "<title>Lettings</title>"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    @pytest.mark.django_db
    def test_letting_view(self, letting):
        client = Client()
        path = reverse("letting", kwargs={"letting_id": 1})
        response = client.get(path)
        content = response.content.decode()
        expected_content = (
            '<h1 class="page-header-ui-title mb-3 display-6">boulangerie du parc</h1>'
        )

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")


class TestLettingsUrls:
    def test_index_url(self):
        path = reverse("index")

        assert path == "/"
        assert resolve(path).view_name == "index"

    def test_lettings_index_url(self):
        path = reverse("lettings_index")

        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings_index"

    @pytest.mark.django_db
    def test_letting_url(self, letting):
        path = reverse("letting", kwargs={"letting_id": 1})

        assert path == "/lettings/1/"
        assert resolve(path).view_name == "letting"


class TestLettingsModels:
    @pytest.mark.django_db
    def test_address_model(self, address):
        expected_value = "34 Rue anatole france"

        assert str(address) == expected_value

    @pytest.mark.django_db
    def test_letting_model(self, letting):
        expected_value = "boulangerie du parc"

        assert str(letting) == expected_value


class TestIntegration:
    @pytest.mark.django_db
    def test_lettings_route(self, letting):
        client = Client()

        lettings_response = client.get("/lettings/")
        single_letting_response = client.get("/lettings/1/")
        data = single_letting_response.content.decode()

        assert lettings_response.status_code == 200
        assert single_letting_response.status_code == 200
        assert "boulangerie du parc" in data
