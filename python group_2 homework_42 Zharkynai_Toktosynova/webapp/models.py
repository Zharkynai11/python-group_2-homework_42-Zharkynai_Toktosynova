from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя')
    password = models.CharField(max_length=200, null=False, blank=False, verbose_name='Пароль')

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(max_length=200, null=False, blank=False, verbose_name='Содержимое')
    author = models.ForeignKey(User, on_delete=models.PROTECT,related_name='author_article')

    def __str__(self):
        return "%s by %s" % (self.title, self.author)

class Comment(models.Model):
    text = models.TextField(max_length=200, null=False, blank=False, verbose_name='Содержимое')
    date = models.DateField(verbose_name="Дата")
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author_comment')
    # comm = models.ForeignKey("self",on_delete=models.PROTECT,blank=True,verbose_name="Комментарий")
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='comment')

    def __str__(self):
        return "%s by %s" % (self.text, self.author)

class Mark(models.Model):
    MARKS = [(1, "Ужасно"), (2, "Плохо"), (3, "Нормально"), (4, "Хорошо"), (5, "Отлично")]
    value = models.IntegerField(choices=MARKS, verbose_name="Оценки")
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор")
    article = models.ForeignKey(Article, on_delete=models.PROTECT, verbose_name="Статья")
    def __str__(self):
        return "%s by %s" % (self.value, self.author)
# Create your models here.
