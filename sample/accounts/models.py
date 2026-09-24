from django.db import models
from django.contrib.auth.models  import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

class CustomUser(AbstractUser):

    email = models.EmailField("メールアドレス", unique=True)
    nickname = models.CharField("ニックネーム", max_length=50, blank=True)
    birth_date = models.DateField("生年月日", null=True, blank=True)

    class Meta:
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー"

    def __str__(self):
        return self.nickname or self.username


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


User = get_user_model()