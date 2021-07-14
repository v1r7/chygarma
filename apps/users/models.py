# from django.conf import settings
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import PermissionsMixin
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class UserManager(BaseUserManager):
#     """Модель Админа"""
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("Users must have an Email address")
#
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, password):
#         user = self.create_user(email=self.normalize_email(email),
#                                 password=password)
#
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     """Модель Пользователей"""
#     first_name = models.CharField(verbose_name='Имя, Фамилия', max_length=255)
#     email = models.EmailField(verbose_name='Почта', max_length=60, unique=True)
#     date_joined = models.DateTimeField(verbose_name='Дата/время регистрации',
#                                        auto_now_add=True)
#     login = models.CharField(verbose_name="Логин", unique=True, max_length=60)
#     last_login = models.DateTimeField(verbose_name='Последний вход',
#                                       auto_now=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'login'
#     REQUIRED_FIELDS = []
#
#     objects = UserManager()
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return self.login
#
# #
# # @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# # def create_auth_token(sender, instance=None, created=False, **kwargs):
# #     if created:
# #         Token.objects.create(user=instance)