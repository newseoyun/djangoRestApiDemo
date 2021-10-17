from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.charField(max_length=30)
    last_name = models.charField(max_length=30)