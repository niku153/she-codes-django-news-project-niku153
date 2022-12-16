# Generated by Django 4.1.3 on 2022-12-14 05:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0009_alter_newsstory_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsstory',
            name='likes',
        ),
        migrations.AddField(
            model_name='newsstory',
            name='like_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked_stories', to=settings.AUTH_USER_MODEL),
        ),
    ]