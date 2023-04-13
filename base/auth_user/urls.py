from django.urls import path
from . import views

urlpatterns = [
    path('api/user', views.registerUser.as_view(), name="registeruser"),
]