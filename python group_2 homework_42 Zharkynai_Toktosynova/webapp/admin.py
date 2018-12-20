from django.contrib import admin
from webapp.models import *

class TopicInLine1(admin.StackedInline):
    model = Comment
    extra = 0

class TopicInLine2(admin.StackedInline):
    model = Mark
    extra = 0

class AdminTopic(admin.ModelAdmin):
    list_display = ["title","text","author"]
    inlines = [TopicInLine1,TopicInLine2]


admin.site.register(User)
admin.site.register(Article, AdminTopic)
admin.site.register(Mark)
admin.site.register(Comment)
# Register your models here.
