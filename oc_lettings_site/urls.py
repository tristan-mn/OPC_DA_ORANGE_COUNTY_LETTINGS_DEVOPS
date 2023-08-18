from django.urls import path, include


urlpatterns = [
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
]


handler404 = "oc_lettings_site.views.error_404"
handler500 = "oc_lettings_site.views.error_500"
