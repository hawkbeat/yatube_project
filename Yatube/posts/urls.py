from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group/posts/', views.group_posts)
] 