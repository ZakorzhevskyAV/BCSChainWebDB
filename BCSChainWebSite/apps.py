from django.apps import AppConfig


# from django_rq import job, get_scheduler, get_queue
# from datetime import datetime


# from django.core.management import call_command


class BcschainwebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BCSChainWebSite'

    """def ready(self):  # Закомментировать это, сделать миграцию, раскомментировать это
        from .tasks import blockchain_update
        from background_task.models import Task
        Task.objects.all().delete()
        blockchain_update()"""
