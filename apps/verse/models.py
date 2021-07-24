from django.conf import settings
from django.db import models

from utils.upload import upload_instance


class Category(models.Model):
    """Модель Категорий"""
    name = models.CharField(verbose_name='Название категории', max_length=255)

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


class AuthorProfile(models.Model):
    """Модель профиля автора"""
    author = models.OneToOneField(Author, on_delete=models.SET_NULL, null=True)
    avatar = models.ImageField(verbose_name='Аватар',
                               upload_to=upload_instance, blank=True, null=True)
    background_picture = models.ImageField(verbose_name='Задний фон',
                                           upload_to=upload_instance,
                                           blank=True, null=True)



class Follower(models.Model):
    """Модель Читателей"""
    value = models.SmallIntegerField("Количеcтво фоловеров", null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'


class Verse(models.Model):
    """Модель Стихов"""
    name = models.CharField(verbose_name='Название', max_length=255)
    content = models.TextField(verbose_name='Содержание')
    views = models.ForeignKey(Follower, verbose_name='Читатели',
                              on_delete=models.SET_NULL, blank=True, null=True)
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


