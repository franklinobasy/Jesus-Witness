from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from witness.models import Editor

from blog.categories import categories as c


def cover_image_path(instance, filename):
    return 'covers/{0}/{1}'.format(instance.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):

    CATEGORIES = c

    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, choices=c)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
            Editor,
            related_name="posts",
            on_delete=models.CASCADE
        )
    cover = models.ImageField(
            upload_to=cover_image_path,
            default='covers/default.jpg'
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    def __str__(self) -> str:
        return self.author.first_name
