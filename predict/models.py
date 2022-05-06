from django.db import models

class Prediction(models.Model):
    file = models.TextField()
    category = models.TextField(max_length=1)
    owner = models.TextField(max_length=16)
