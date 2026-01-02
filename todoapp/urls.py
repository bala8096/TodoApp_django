
from django.urls import path

from . import views

urlpatterns = [
     path('',views.home, name='home'),
    path('list/',views.todo_list, name='todo_list'),
    path('create_todo/',views.todo_create, name='todo_create'),
    path('update_todo/<int:id>/',views.todo_update, name='todo_update'),
    path('delete_todo/<int:id>/',views.todo_delete, name='todo_delete'),
]