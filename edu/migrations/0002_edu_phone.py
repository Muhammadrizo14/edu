# Generated by Django 3.2.9 on 2021-12-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edu',
            name='phone',
            field=models.CharField(default=0, max_length=150, verbose_name='Телефон номер ученика'),
        ),
    ]
