# Generated by Django 3.2.2 on 2021-07-26 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verse', '0007_alter_like_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='verse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verse.verse', verbose_name='Стих'),
        ),
    ]
