from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todoapp/', views.todo),
    path('addTodoItems/', views.addTodoView),
    path('deleteTodoItem/<int:i>/',views.deleteTodo)
]
