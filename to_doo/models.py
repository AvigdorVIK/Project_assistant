from django.db import models

class Tasks(models.Model):
    name = models.TextField (blank=True)

