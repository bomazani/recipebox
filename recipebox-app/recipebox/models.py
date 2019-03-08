from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    bio = models.CharField(max_length=124)

    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    title = models.CharField(max_length=124)
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} - by {self.author.user.username}"
