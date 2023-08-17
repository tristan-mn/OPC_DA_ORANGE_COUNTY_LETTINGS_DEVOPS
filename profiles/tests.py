import pytest
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile


@pytest.fixture
def profile():
    user = User.objects.create_user(username='fritas', first_name='Manu', last_name='Lebelge',
                                    email='fritas@lebelge.com')
    profile = Profile.objects.create(user=user, favorite_city='Bruxelles')
    return profile


class TestProfilesViews:
    @pytest.mark.django_db
    def test_profiles_index_view(self):
        client = Client()
        path = reverse('profiles_index')
        response = client.get(path)
        content = response.content.decode()
        expected_content = '<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>'


        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")
    
    
    @pytest.mark.django_db
    def test_profile_view(self, profile):
        client = Client()
        path = reverse('profile', kwargs={'username': "fritas"})
        response = client.get(path)
        content = response.content.decode()
        expected_content = '<h1 class="page-header-ui-title mb-3 display-6">fritas</h1>'

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")


class TestProfilesUrls:
    def test_profiles_index_url(self):
        path = reverse('profiles_index')
        
        assert path == "/profiles/"
        assert resolve(path).view_name == "profiles_index"

    @pytest.mark.django_db
    def test_profile_url(self, profile):
        path = reverse('profile',  kwargs={'username': 'fritas'})
        
        assert path == "/profiles/fritas/"
        assert resolve(path).view_name == "profile"


class TestProfilesModel:
    @pytest.mark.django_db
    def test_profile_model(self, profile):
        client = Client()
        expected_value = "fritas"

        assert str(profile) == expected_value


class TestIntegration:
    
    @pytest.mark.django_db
    def test_profiless_route(self, profile):
        client = Client()

        profiles_response = client.get('/profiles/')
        single_profile_response = client.get('/profiles/fritas/')
        data = single_profile_response.content.decode()

        assert profiles_response.status_code == 200
        assert single_profile_response.status_code == 200
        assert "fritas" in data
