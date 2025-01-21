from django.db import models


class TaskQuerySet(models.QuerySet):
    def less_than_priority(self, priority):
        return self.filter(priority__lt=priority)

    def without_status(self, status='Completed'):
        return self.filter(status__ne=status)



class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model)

    def less_than_year(self, year):
        return self.get_queryset().less_than_priority(year)

    def without_status(self, status):
        return self.get_queryset().without_status(status)
