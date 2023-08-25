from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    '''A topic user is learning about'''
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """return a string representation of a model"""
        return self.text


class Entry(models.Model):
    """something specific learnt about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.text[:51]
