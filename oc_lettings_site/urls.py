from django.urls import path

from oc_lettings_site import views

app_name = "oc_lettings_site"

urlpatterns = [
    path("", views.index, name="index"),
]
