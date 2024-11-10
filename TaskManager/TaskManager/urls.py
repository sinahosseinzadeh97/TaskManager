from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Include URLs from the tasks app
    path('', lambda request: redirect('task_list')),  # Redirect root URL to task_list
]
