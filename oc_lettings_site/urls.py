from django.urls import path, include
from django.conf.urls import handler404, handler500


def test(request):
    division = 1 / 0

urlpatterns = [
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path("test/", test)
]


handler404 = 'oc_lettings_site.views.error_404'
handler500 = 'oc_lettings_site.views.error_500'
