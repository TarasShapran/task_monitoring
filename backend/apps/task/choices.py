from django.db import models
from django.utils.regex_helper import Choice


class TaskStatusChoice(models.TextChoices):
    Pending = 'Pending'
    ToDo = 'ToDo'
    InProgress = 'InProgress'
    Completed = 'Completed'
