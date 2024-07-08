from django.db import models

class Task(models.Model):
    heading = models.CharField(max_length=200)
    details = models.TextField()

    def __str__(self):
        return self.heading
