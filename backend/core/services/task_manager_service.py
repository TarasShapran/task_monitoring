from configs.celery import app, logger

from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Count, Q

from apps.task.choices import TaskStatusChoice
from apps.task.models import TaskModel

UserModel = get_user_model()


class TaskService:

    @staticmethod
    @app.task(bind=True, max_retries=1, default_retry_delay=2)
    def _manage_task(self, task_id):
        try:
            logger.info(f'Starting task {self.name}...')
            with transaction.atomic():
                task = TaskModel.objects.select_for_update().get(id=task_id)

                user = UserModel.objects.annotate(
                    task_count=Count('tasks', filter=~Q(tasks__status=TaskStatusChoice.Completed))
                ).filter(
                    task_count__lt=UserModel.get_max_tasks()
                ).order_by('-task_count').first()

                if user:
                    logger.info(f'Start assigne to user {user}')
                    task.user = user
                    task.status = TaskStatusChoice.ToDo
                    task.save()
                else:
                    logger.info('No user found for task assignment')
                    task.status = TaskStatusChoice.Pending
                    task.save()
                    return

        except Exception as e:
            logger.error(f'Error while managing task: {e}')
            self.retry(countdown=2)

    @classmethod
    def handle_task(cls, task_id):
        cls._manage_task.apply_async((task_id,))

    @staticmethod
    @app.task
    def assign_task_to_user():
        tasks = TaskModel.objects.filter(user=None).order_by('priority')
        for task in tasks:
            TaskService._manage_task.apply_async((task.id,))
