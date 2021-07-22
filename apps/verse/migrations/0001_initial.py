# Generated by Django 3.2.2 on 2021-07-22 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.upload


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Хештег',
                'verbose_name_plural': 'Хештеги',
            },
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('description', models.TextField(blank=True, max_length=70, verbose_name='Описание')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=utils.upload.upload_instance, verbose_name='Изображение')),
                ('pubdate', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('recommend', models.BooleanField(default=False, verbose_name='рекомендация произведения')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_name', to='verse.author', verbose_name='Автор')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='verse.category', verbose_name='Категория')),
                ('tags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='verse.tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Стих',
                'verbose_name_plural': 'Стихи',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(default=0)),
                ('verse', models.ForeignKey(on_delete=models.SET(-1), to='verse.verse', verbose_name='Стих')),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=444, verbose_name='Коментарий')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verse.author')),
                ('verse', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='verse.verse', verbose_name='Комментарий к стиху')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=utils.upload.upload_instance, verbose_name='Аватар')),
                ('background_picture', models.ImageField(blank=True, null=True, upload_to=utils.upload.upload_instance, verbose_name='Задний фон')),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='verse.author')),
                ('readers', models.ManyToManyField(related_name='readers', to='verse.Author')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
