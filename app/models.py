from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200) 
    low_text = models.CharField(max_length=160, default='text')
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_creation = models.DateTimeField(default=timezone.now)
    time_publication = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.time_publication = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

