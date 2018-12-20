# Generated by Django 2.1.4 on 2018-12-20 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=200, verbose_name='Содержимое')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200, verbose_name='Содержимое')),
                ('date', models.DateField(verbose_name='Дата')),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.Article', verbose_name='Статья')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(choices=[(1, 'Ужасно'), (2, 'Плохо'), (3, 'Нормально'), (4, 'Хорошо'), (5, 'Отлично')], verbose_name='Оценки')),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='webapp.Article', verbose_name='Статья')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('password', models.CharField(max_length=200, verbose_name='Пароль')),
            ],
        ),
        migrations.AddField(
            model_name='mark',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.User', verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author_comment', to='webapp.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comm',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='webapp.Comment', verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author_article', to='webapp.User'),
        ),
    ]
