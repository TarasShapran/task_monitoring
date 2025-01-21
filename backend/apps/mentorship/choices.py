from django.db import models
from django.utils.regex_helper import Choice


class FormatMentorChoice(models.TextChoices):
    OfflineMentoring = 'OfflineMentoring'
    VideoMentoring = 'VideoMentoring'
    ChatMentoring = 'ChatMentoring'

