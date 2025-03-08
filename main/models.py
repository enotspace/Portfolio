from django.conf import settings
from django.db import models as m
from django.utils import timezone

class Projects(m.Model):
    title = m.CharField(max_length=200)
    link = m.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class formmodel(m.Model):
    first_name = m.CharField(max_length=50)
    last_name = m.CharField(max_length=100)
    text = m.TextField()
    datecreated = m.DateTimeField(default=timezone.now())