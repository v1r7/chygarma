from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.upload import upload_instance



class Category(models.Model):
    """Модель Категорий"""
    name = models.CharField(max_length=60, blank=True,
                             verbose_name="Категории")

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
    author = models.OneToOneField(Author, on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='profile_user')
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

    tags = models.ForeignKey(Tag, verbose_name='Хэштэги',
                             on_delete=models.SET_NULL,
                             null=True)
    is_liked = models.ManyToManyField(Author, related_name='likes', verbose_name='Лайки')
    picture = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_instance, blank=True, null=True)
    pubdate = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    recommend = models.BooleanField(default=False, verbose_name='рекомендация произведения')

    class Meta:
        verbose_name = 'Стих'
        verbose_name_plural = 'Стихи'

    def __str__(self):
        return self.name

    def verse_picture_or_default(self, default_path="/media/uploads/verse/default/default.png"):
        if self.picture:
            return self.picture
        return default_path


class Comment(models.Model):
    """ Модель Коментарий"""
    content = models.CharField(verbose_name='Коментарий', max_length=444)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='comments_author',
                               null=True)
    verse = models.ForeignKey(Verse, verbose_name="Комментарий к стиху",
                              on_delete=models.CASCADE, null=True)
    create_at = models.DateField(auto_now_add=True, verbose_name='Дата публикации', null=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return f'{self.content[:100]}...'


class News(models.Model):
    """Модель новостей"""
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(max_length=333, verbose_name='Содержание')
    picture = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_instance, blank=True, null=True)
    main_page_filter = models.BooleanField(default=False, verbose_name='Рекомендация новости')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title



