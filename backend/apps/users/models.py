from datetime import date

from core.enums.regex_enum import RegEx
from core.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from apps.users.managers import UserManager


class MentorProfileModel(BaseModel):
    class Meta:
        db_table = 'mentor_profile'

    experience = models.TextField()
    specialization = models.ManyToManyField('mentorship.SpecializationModel')
    technology_stack = models.ManyToManyField('mentorship.TechnologyStackModel')


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    birth_day = models.DateField()

    @property
    def get_age(self):
        if self.birth_day:
            today = date.today()
            age = today.year - self.birth_day.year - (
                    (today.month, today.day) < (self.birth_day.month, self.birth_day.day))
            return age
        return None


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    MAX_TASKS = 10

    class Meta:
        db_table = 'auth_user'
        ordering = ['id']

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[
        V.RegexValidator(*RegEx.PASSWORD.value)
    ])
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user', null=True)
    mentor_profile = models.OneToOneField(MentorProfileModel, on_delete=models.CASCADE, related_name='user', null=True)

    @classmethod
    def get_max_tasks(cls):
        return cls.MAX_TASKS

    USERNAME_FIELD = 'email'
    objects = UserManager()
