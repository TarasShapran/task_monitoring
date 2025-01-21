from django.urls import path

from .views import *

urlpatterns = [
    path('/servise', MentoringServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='users_list_create'),
    path('/servise/<int:pk>', MentoringServiceViewSet.as_view({'get': 'list', 'post': 'create', 'patch': 'partial_update'}), name='users_list_create'),
]