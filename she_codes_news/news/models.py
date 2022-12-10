from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
    class Meta:
        ordering = ['-pub_date']
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()

