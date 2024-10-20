from django.db import models

class user(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.PositiveBigIntegerField()
    password = models.CharField(max_length=16)

class query(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField()

class property_booking_details(models.Model):
    user = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.PositiveBigIntegerField()
    category = models.CharField(max_length=255)
    p_id = models.CharField(max_length=50)
    