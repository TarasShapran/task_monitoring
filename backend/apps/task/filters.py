
from django_filters import rest_framework as filters

from apps.task.choices import TaskStatusChoice
from apps.task.models import TaskModel


class TaskFilter(filters.FilterSet):
    priority_range = filters.RangeFilter('priority') # range_min=2000&range_max=2010
    priority_in = filters.BaseInFilter('priority') # priority_in=1
    status_type = filters.ChoiceFilter('status_type', choices=TaskStatusChoice.choices)
    order = filters.OrderingFilter(
        fields=(
            'id',
            'priority',
            'status'
        )
    ) # order=-id


# TaskModel.objects.filter(model__endswith=)