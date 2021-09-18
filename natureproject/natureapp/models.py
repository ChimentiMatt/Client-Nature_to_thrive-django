from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, default='See more by clicking on the link below')
    body = models.TextField()
    event_date = models.DateTimeField(default=now, blank=True)
    image = models.ImageField(upload_to='images/', default='images/cat.jpg')
    location = models.CharField(max_length=255, default="1234 Fake Drive, Portland Oregon, 97065")

    def __str__(self):
        return self.title 

