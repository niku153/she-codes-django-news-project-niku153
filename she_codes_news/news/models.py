from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



class NewsStory(models.Model):
    class Meta:
        ordering = ['-pub_date']
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    # author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(null=True)
    category = models.CharField(max_length=200, default='uncategorised')
    liked_by = models.ManyToManyField(CustomUser, related_name='liked_stories', blank=True, null=True )


class Comment(models.Model):
    post = models.ForeignKey(NewsStory, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)



