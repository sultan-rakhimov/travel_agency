# Generated by Django 3.0.5 on 2020-05-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteviewer', '0013_auto_20200426_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last Name')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]