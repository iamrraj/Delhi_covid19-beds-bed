from django.urls import path, re_path as url
from . import views as view

urlpatterns = [
    path("bed/data/", view.ViewBedss.as_view()),
    path("details/", view.ViewHospitals.as_view()),
    # path("data/<uuid:idd>/",view.ViewHospital.as_view())
]