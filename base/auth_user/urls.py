from django.urls import path
from . import views_api, views_form

urlpatterns = [
    path('', views_form.index, name='index'),
    path('api/user', views_api.getUser.as_view(), name="getuser"),
    path('api/usercreate', views_api.registerUser.as_view(), name="registeruser"),
    path('api/user/<str:uid>', views_api.editUser.as_view(), name="edituser"),
    path('api/user/<str:uid>', views_api.deleteUser.as_view(), name="edituser"),
    path('api/login', views_api.loginAPI.as_view(), name = 'login'),
    path('register/', views_form.register, name="register")
   ]