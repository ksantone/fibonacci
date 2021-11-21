from django.db import models

# Create your models here.
class AlgorithmProgress(models.Model):
	percent = models.IntegerField(default=0)
	pipeline = models.CharField(default="", max_length=20)
	algorithm_number = models.IntegerField(default=0)