from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.upload import upload_instance

# category = (
#     ('1', 'о любви'),
#     ('2', 'о войне'),
#     ('3', 'о природе'),
#     ('4', 'для детей'),
#     ('1', 'о Родине'),
#     ('2', 'о жизни'),
#     ('1', 'о смерти'),
#     ('2', 'о себе'),
#     )

class Category(models.Model):
    """Модель Категорий"""
    name = models.CharField(max_length=60, blank=True,
                             verbose_name="Категории")
    # , choices = category,

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tag(models.Model):
    """Модели Тэгов """
    name = models.CharField(verbose_name='Тэги', max_length=255)

    class Meta:
        verbose_name = 'Хештег'
        verbose_name_plural = 'Хештеги'

    def __str__(self):
        return self.name


class Author(models.Model):
    """Модель Автора"""
    author = models.OneToOneField(settings.AUTH_USER_MODEL,
                                  on_delete=models.SET_NULL,
                                  related_name='author',
                                  null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.author.__str__()


@receiver(post_save, sender=Author)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        AuthorProfile.objects.create(author=instance)


class AuthorProfile(models.Model):
    """Модель профиля автора"""
    author = models.OneToOneField(Author, on_delete=models.SET_NULL, null=True)
    avatar = models.ImageField(verbose_name='Аватар',
                               upload_to=upload_instance, blank=True, null=True)
    background_picture = models.ImageField(verbose_name='Задний фон',
                                           upload_to=upload_instance,
                                           blank=True, null=True)
    readers = models.ManyToManyField(to=Author, related_name='readers')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.author.__str__()}'



class Verse(models.Model):
    """Модель Стихов"""
    name = models.CharField(verbose_name='Название', max_length=255)
    content = models.TextField(verbose_name='Содержание')
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL,
                                 null=True)
    author = models.ForeignKey(Author, related_name='author_name', verbose_name='Автор',
                                 on_delete=models.SET_NULL,
                                 null=True)
    description = models.TextField(verbose_name='Описание', blank=True, max_length=70)

    tags = models.ForeignKey(Tag, verbose_name='Тэги',
                             on_delete=models.SET_NULL,
                             null=True)
    picture = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_instance, blank=True, null=True )
    pubdate = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    recommend = models.BooleanField(default=False, verbose_name='рекомендация произведения')

    class Meta:
        verbose_name = 'Стих'
        verbose_name_plural = 'Стихи'

    def __str__(self):
        return self.name


class Comment(models.Model):
    """ Модель Коментарий"""
    content = models.CharField(verbose_name='Коментарий', max_length=444)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    verse = models.ForeignKey(Verse, verbose_name="Комментарий к стиху",
                              on_delete=models.CASCADE, null=True)
    create_at = models.DateField(auto_now_add=True, verbose_name='Дата публикации', null=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.content


class Like(models.Model):
    """Модель Лайков"""
    like = models.IntegerField(default=0)
    verse = models.ForeignKey(Verse, verbose_name="Стих", on_delete=models.SET(-1))


    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return self.like


