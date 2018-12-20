# Generated by Django 2.1.4 on 2018-12-20 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20181220_0350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comm',
        ),
        migrations.AddField(
            model_name='article',
            name='comm',
            field=models.ForeignKey(default='124', on_delete=django.db.models.deletion.PROTECT, related_name='comment', to='webapp.Comment'),
        ),
        migrations.RemoveField(
            model_name='article',
            name='marks',
        ),
        migrations.AddField(
            model_name='article',
            name='marks',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='mark', to='webapp.Mark'),
        ),
    ]
