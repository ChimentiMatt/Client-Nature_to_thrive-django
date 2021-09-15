from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    event_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title 

