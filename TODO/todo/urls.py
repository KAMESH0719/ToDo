from django.urls import path
from . import views

urlpatterns = [
    # add task
    path('addtask/', views.addTask, name='addTask'),
    # mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # mark as Undone
    path('mark_as_Undone/<int:pk>/', views.mark_as_Undone, name='mark_as_Undone'),
    # Edit feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # delete task
     path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
