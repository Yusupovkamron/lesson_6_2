from django.db import models
class book(models.Model):
    title = models.CharField(max_length=20, null=True)
    desciption = models.TextField

# Create your models here.
