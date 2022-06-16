from django.db import models

class User(models.model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

class Mentor(models.model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

class Mentee(models.model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)