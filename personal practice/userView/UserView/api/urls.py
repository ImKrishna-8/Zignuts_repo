from django.urls import path,include
from . import views
urlpatterns = [
    path('users',views.UserViewTest.as_view()),
    path('users/<int:id>',views.UserUpdateView.as_view()),
]