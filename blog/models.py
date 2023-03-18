from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from witness.models import Editor


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
            Editor,
            related_name="posts",
            on_delete=models.CASCADE
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Editor, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self) -> str:
        return self.author.first_name