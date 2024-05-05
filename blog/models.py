# blog/models.py

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Provide unique related_name arguments for ForeignKey fields
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
