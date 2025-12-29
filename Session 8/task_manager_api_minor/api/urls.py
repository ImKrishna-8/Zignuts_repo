from django.urls import path,include
from . import views


urlpatterns = [
    path('users/',views.UserView.as_view()),
    path('tasks/',views.TodoView.as_view()),
    
    path('tasks/<int:id>',views.TodoView.as_view()),

]
