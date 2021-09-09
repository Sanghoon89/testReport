# Generated by Django 3.2.6 on 2021-08-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG'),
        ),
    ]
