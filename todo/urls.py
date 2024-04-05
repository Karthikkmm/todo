from django.urls import path
from . import views

urlpatterns = [
    # to add task
    path('addTask/',views.addTask,name='addTask'),

    # to mark the task as done and move to completed task
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),

    #to mark the task as undone and move task to be completed 
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),

    # to edit the task using button
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),

    # to delete the task
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
] 