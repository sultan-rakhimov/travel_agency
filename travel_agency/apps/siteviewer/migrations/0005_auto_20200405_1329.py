# Generated by Django 3.0.4 on 2020-04-05 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteviewer', '0004_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]