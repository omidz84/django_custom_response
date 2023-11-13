from django.urls import path

from . import views

urlpatterns = [
    path('', views.TestResponse.as_view())
]
