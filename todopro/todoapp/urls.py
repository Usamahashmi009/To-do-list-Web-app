from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/add/', views.add_blog, name='add_blog'),
]