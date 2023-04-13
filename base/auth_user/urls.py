from django.urls import path
from . import views

urlpatterns = [
    path('api/user', views.getUser.as_view(), name="getuser"),
    path('api/usercreate', views.registerUser.as_view(), name="registeruser"),
]