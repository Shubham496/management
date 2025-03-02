from django.urls import path
from . import views


urlpatterns = [
   # path('', views.HomeViewApi.as_view(), name='home'),
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]

