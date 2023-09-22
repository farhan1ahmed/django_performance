from django.urls import path

from .views import AuthorsApiView

urlpatterns = [
    path("", AuthorsApiView.as_view(), name="authors-view"),
    ]