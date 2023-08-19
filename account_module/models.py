from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    mobile = models.IntegerField(max_length=20, verbose_name='تلفن همراه'),
    email_active_code = models.CharField(max_length=300, verbose_name='فعالسازی ایمل')
    avatar = models.ImageField(null=True, upload_to='images/profiles', verbose_name='تصویر  کاربر')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره کاربر')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):

        return self.username
