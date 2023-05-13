from django.db import models
from django.utils import timezone # imporing timezone to get the time each entry is made

# Create your models here.

class Entry(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    date_created = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return f"{self.title}"
    
