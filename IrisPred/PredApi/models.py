from django.db import models

# Create your models here.

class specs(models.Model):
    sepal_length = models.FloatField(default=0)
    sepal_width = models.FloatField(default=0)
    petal_length = models.FloatField(default=0)
    petal_width = models.FloatField(default=0)
    classification = models.CharField(default=0,max_length=30)

    def __str__(self):
        return self.classification