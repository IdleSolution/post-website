from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=15)
    profile_description = models.TextField()
    created_date = models.DateTimeField()
    followers_count = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Post(models.Model):
    who_wrote_it = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    posted_date = models.DateTimeField()
    like_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
