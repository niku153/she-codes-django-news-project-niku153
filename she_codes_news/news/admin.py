from django.contrib import admin

from .models import NewsStory, Comment, Category

admin.site.register(NewsStory)
admin.site.register(Comment)
admin.site.register(Category)


# Register your models here.
