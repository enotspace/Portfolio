from django.conf import settings
from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title