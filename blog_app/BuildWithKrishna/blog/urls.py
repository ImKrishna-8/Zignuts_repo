from django.contrib import admin
from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('search', views.search, name="search"),
    path('login', views.loginHandler, name="login"),
    path('logout/', views.logoutHandler, name="logout"),
    path('signup', views.signup, name="signup"),
    path('createPost', views.createPost, name="createPost"),
    path('create', views.create, name="create"),
    path('yourpost', views.yourpost, name="yourpost"),
    path('allpost', views.allpost, name="allpost"),
    path('detail/<int:post_id>',views.detail,name="detail"),
    path('edit/<int:post_id>',views.edit,name="edit"),
    path('delete/<int:post_id>',views.delete,name="delete"),
    path('update/<int:post_id>', views.update, name="update"),
]