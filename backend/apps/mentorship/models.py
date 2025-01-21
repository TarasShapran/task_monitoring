from django.db import models

from apps.mentorship.choices import FormatMentorChoice
from apps.users.models import MentorProfileModel, UserModel


class SpecializationModel(models.Model):
    class Meta:
        db_table = 'specialization'

    name = models.CharField(max_length=50)


# Technology stack model
class TechnologyStackModel(models.Model):
    class Meta:
        db_table = 'technology_stack'

    name = models.CharField(max_length=50)


class MentoringServiceModel(models.Model):
    class Meta:
        db_table = 'mentoring_service'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='mentoring_service')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class MentorshipFormatModel(models.Model):
    class Meta:
        db_table = 'mentorship_format'

    formats = models.CharField(max_length=30, choices=FormatMentorChoice.choices)
    mentoring_service = models.ForeignKey(MentoringServiceModel, on_delete=models.CASCADE,
                                          related_name='mentorship_formats')
