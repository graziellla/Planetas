# Generated by Django 2.2.1 on 2019-05-17 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planeta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composicao',
            name='nome',
        ),
    ]