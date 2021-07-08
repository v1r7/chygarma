from django.db import models


from utils.upload import upload_instance

class Picture(models.Model):
    """Модель Картинок"""
    image = models.ImageField(verbose_name='Изображение',
                              upload_to=upload_instance)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.id} - image'


class Author(models.Model):
    """Модель Автора"""
    name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    picture = models.ManyToManyField(Picture, related_name='authors_pic', verbose_name='Аватар')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name

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

class Like(models.Model):
    """Модель Лайков"""
    like = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Хештег'
        verbose_name_plural = 'Хештеги'

    def __str__(self):
        return self.like

class Viewer(models.Model):
    """Модель Читателей"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'
        ordering = ["-value"]

class Verse(models.Model):
    """Модель Стихов"""
    name = models.CharField(verbose_name='Название', max_length=255)
    content = models.TextField(verbose_name='Содержание')
    views = models.ForeignKey(Viewer,verbose_name='Читатели',
                              on_delete=models.CASCADE, default=0)
    authors = models.ManyToManyField(Author, verbose_name='Автор произведения')
    description = models.TextField(verbose_name='Описание',)

    tags = models.ForeignKey(Tag, verbose_name='Тэги',
                             on_delete=models.SET_NULL,
                             null=True)
    picture = models.ManyToManyField(Picture, related_name='product_pictures',
                                     verbose_name='Иллюстрация')
    pubdate = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    like = models.ForeignKey(Like, verbose_name='Нравится',
                             on_delete=models.SET_NULL,
                             null=True)

    class Meta:
        verbose_name = 'Стих'
        verbose_name_plural = 'Стихи'

    def __str__(self):
        return self.name


class Comment(models.Model):
    """ Модель Коментарий"""
    content = models.CharField(verbose_name='Коментарий', max_length=444)
    author = models.ForeignKey(Author, verbose_name='Автор',
                               on_delete=models.SET_NULL,
                               null=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.content