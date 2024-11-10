from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),          # List all tasks
    path('add/', views.add_task, name='add_task'),         # Add a new task
    path('<int:pk>/edit/', views.edit_task, name='edit_task'),  # Edit a task
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),  # Delete a task
]
