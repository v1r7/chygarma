from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from utils.upload import upload_instance


class UserManager(BaseUserManager):
    """
        This is a manager for Account class
    """

    def create_user(self, login, email=None, password=None):

        if not login:
            raise ValueError("User must enter login")
        email = UserManager.normalize_email(email)

        user = self.model(login=login, email=email,
                          is_staff=False, is_active=True, is_superuser=False,)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, login, password):
        user = self.create_user(
            login,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Модель Пользователей и Авторов"""
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    email = models.EmailField(verbose_name='Почта', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='Дата/время регистрации',
                                       auto_now_add=True)
    avatar = models.ImageField(verbose_name='Аватар',
                                upload_to=upload_instance)
    background_picture = models.ImageField(verbose_name='Задний фон',
                                upload_to=upload_instance)
    warning = models.BooleanField(default=False, verbose_name='предупреждение')
    login = models.CharField(verbose_name="Логин", max_length=60, unique=True)
    last_login = models.DateTimeField(verbose_name='Последний вход',
                                      auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = UserManager()


    class Meta:
        verbose_name = 'Пользователь/автор'
        verbose_name_plural = 'Пользователи/авторы'

    def __str__(self):
        return u"%s %s"% (self.first_name, self.last_name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)