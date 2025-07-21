from django.db import models

# Create your models here.

class Room(models.Model):
    #host = 
    #topic =
    name = models.CharField(max_length=200)
    descriptioon = models.TextField(null=True, blank=True)
    #participants =
    updated = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    #user = 
    room = models.ForeignKey(Room)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]