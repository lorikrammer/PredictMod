from django.urls import path

from . import views

urlpatterns = [
    path("", views.ui, name="index"),
    path("mg-upload/", views.mg_upload, name="mg-upload"),
    path("ehr-upload/", views.ehr_upload, name="ehr-upload"),
]
