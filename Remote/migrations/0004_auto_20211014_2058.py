# Generated by Django 3.2.6 on 2021-10-14 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Remote', '0003_auto_20211008_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keep',
            name='safein_chk',
            field=models.CharField(choices=[('o', '입고확인'), ('x', '입고대기'), ('w', 'Withdrawn')], default='x', max_length=1, verbose_name='Check in coffer'),
        ),
        migrations.AlterField(
            model_name='keep',
            name='safeout_chk',
            field=models.CharField(default='x', max_length=1, verbose_name='Check out coffer'),
        ),
    ]