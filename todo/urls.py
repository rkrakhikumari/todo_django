from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index' ),
    path('toggle_task/<int:id>/', toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', delete_task, name="delete_task")
]
