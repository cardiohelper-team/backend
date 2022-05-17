from django.db import models

class Prediction(models.Model):
    file = models.TextField()
    category = models.TextField(max_length=1)
    user = models.TextField(max_length=16)
    date = models.DateTimeField(auto_now_add=True)
