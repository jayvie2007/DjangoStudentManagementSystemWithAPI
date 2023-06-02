from django.urls import path
from . import views_api, views_form

# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'api/v1/payment/(?P<state>[^/.]+)', views_api.StatusPageViewSet, basename='payment')

urlpatterns = [
    #Templates
    path('', views_form.index, name='index'),
    path('register/', views_form.register, name="register_user"),
    path('login/', views_form.login_view, name="login_user"),
    path('logout/', views_form.logout_view, name="logout_user"),
    
    #API
    path('api/user', views_api.getUser.as_view(), name="get_user"),
    path('api/usercreate', views_api.registerUser.as_view(), name="register_api"),
    path('api/user/<str:uid>', views_api.editUser.as_view(), name="edit_api"),
    path('api/user/<str:uid>', views_api.deleteUser.as_view(), name="delete_api"),
    path('api/login', views_api.loginAPI.as_view(), name = 'login_api'),
    
    # Templates
    path('database/', views_form.database, name="database"),
    path('database/add/', views_form.add, name="add"),
    path('database/edit/<str:student_number>', views_form.edit, name ="edit"),
    path('datebase/delete/<str:student_number>', views_form.delete, name ="delete"),
    
    # API
    path('api/student/', views_api.getStudent.as_view(), name="databaseStudent"),
    path('api/student/add/', views_form.add, name="addStudent"),
    path('api/student/edit/<str:student_number>', views_form.edit, name ="editStudent"),
    path('api/student/delete/<str:student_number>', views_form.delete, name ="deleteStudent"),
]