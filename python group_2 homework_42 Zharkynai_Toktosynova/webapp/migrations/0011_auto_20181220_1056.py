# Generated by Django 2.1.4 on 2018-12-20 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='marks',
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]