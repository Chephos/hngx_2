from django.urls import path

from . import views

urlpatterns = [
    path("", views.PersonCreate.as_view()),
    path("<int:pk>/", views.PersonDetail.as_view())
]