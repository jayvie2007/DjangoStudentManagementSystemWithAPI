from django.urls import path
from . import views

urlpatterns = [
    path('api/user', views.getUser.as_view(), name="getuser"),
    path('api/usercreate', views.registerUser.as_view(), name="registeruser"),
    path('api/user/<str:uid>', views.editUser.as_view(), name="edituser"),
    path('api/user/<str:uid>', views.deleteUser.as_view(), name="edituser"),
    path('api/login', views.loginAPI.as_view(), name = 'login')
   ]