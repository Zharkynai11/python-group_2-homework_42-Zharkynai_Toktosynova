# Generated by Django 2.1.4 on 2018-12-20 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20181220_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='comm',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]