from django.urls import path

from .views import ListUsersTasksView, TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskStatisticView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='tasks_create_list'),
    path('/<int:pk>', TaskRetrieveUpdateDestroyView.as_view(), name='tasks_retrieve_update_destroy_list'),
    path('/my_tasks', ListUsersTasksView.as_view(), name='tasks_retrieve_my_list'),
    path('/statistic', TaskStatisticView.as_view(), name='task_statistic'),
]
