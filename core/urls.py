from django.urls import path
from .views.subject_view import subject_detail, subject_list, subject_register

urlpatterns = [
    path("subject/<int:subject_id>/", subject_detail, name="subject"),
    path("subjects/", subject_list, name = "subject_list"),
    path("subject/register/",subject_register, name = "subject_register" )
]
