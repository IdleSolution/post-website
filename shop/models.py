from django.db import models
from post.models import User
from django.template.defaultfilters import slugify

class Item(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    description = models.TextField()
    who_sold_it = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
