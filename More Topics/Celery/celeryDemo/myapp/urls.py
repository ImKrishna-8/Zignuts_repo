from . import views

from django.urls import path,include
urlpatterns = [
    path('', views.index),
    path("result/<str:id>/", views.result,name='result')

]
