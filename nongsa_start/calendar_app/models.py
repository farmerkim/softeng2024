from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
