from django.urls import path
from . import views_api, views_form

urlpatterns = [
    path('', views_form.index, name='index'),
    path('api/user', views_api.getUser.as_view(), name="get_user"),
    path('api/usercreate', views_api.registerUser.as_view(), name="register_api"),
    path('api/user/<str:uid>', views_api.editUser.as_view(), name="edit_api"),
    path('api/user/<str:uid>', views_api.deleteUser.as_view(), name="delete_api"),
    path('api/login', views_api.loginAPI.as_view(), name = 'login_api'),
    path('register/', views_form.register, name="register_user"),
    path('login/', views_form.login, name="login_user"),
    path('logout/', views_form.logout, name="logout_user"),
    path('database/', views_form.database, name="database"),
   ]