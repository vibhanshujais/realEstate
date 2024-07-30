from django.db import models

class user(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.PositiveBigIntegerField()
    password = models.CharField(max_length=16)