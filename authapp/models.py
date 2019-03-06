

from django.db import models
from django.contrib.auth.models import AbstractUser


class UrchinUser(AbstractUser):
    age = models.PositiveSmallIntegerField(verbose_name='возраст')
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
