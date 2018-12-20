# Generated by Django 2.1.4 on 2018-12-20 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20181220_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comment', to='webapp.Comment'),
        ),
        migrations.AlterField(
            model_name='article',
            name='marks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mark', to='webapp.Mark'),
        ),
    ]
