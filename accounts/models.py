from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """拡張ユーザーモデル"""

    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'

    age = models.IntegerField('年齢', blank=True, null=True)
