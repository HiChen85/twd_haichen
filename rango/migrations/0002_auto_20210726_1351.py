# Generated by Django 2.1.5 on 2021-07-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='likes'),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0, verbose_name='views'),
        ),
    ]
