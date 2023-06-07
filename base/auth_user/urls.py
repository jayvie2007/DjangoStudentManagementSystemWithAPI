from django.urls import path, include
from . import views_api, views_form

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'api/user', views_api.StatusPageViewUserAPI, basename='fetchUserAPI'),
router.register(r'api/student', views_api.StatusPageViewStudentAPI, basename='fetchStudentAPI'),
router.register(r'api', views_api.StatusPageViewLoginUserAPI, basename='LoginAPI'),

urlpatterns = [
    #Templates
    path('', views_form.index, name='index'),
    path('register/', views_form.register, name="register_user"),
    path('login/', views_form.login_view, name="login_user"),
    path('logout/', views_form.logout_view, name="logout_user"),
    
    path('database/', views_form.database, name="database"),
    path('database/add/', views_form.add, name="add"),
    path('database/edit/<str:student_number>', views_form.edit, name ="edit"),
    path('datebase/delete/<str:student_number>', views_form.delete, name ="delete"),

    #API
    path('', include(router.urls)),
    path('api/user/edit_user/<str:uid>/', views_api.StatusPageViewUserAPI.as_view({'put': 'edit_user'}), name='edit-user'),
    path('api/user/delete_user/<str:uid>/', views_api.StatusPageViewUserAPI.as_view({'delete': 'delete_user'}), name='edit-user'),
]