from django.contrib import admin
from django.urls import path 
from todo.views import TodoIndexView, TodoListView, TodoDetailView


app_name = 'todo'

urlpatterns =[
    path('', TodoIndexView.as_view(), name='index'),
    path('list/', TodoListView.as_view(), name='list'),
    path('detail/<int:pk>/', TodoDetailView.as_view(), name='detail')
    
]