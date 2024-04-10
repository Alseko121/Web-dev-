from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField()
    address = models.TextField()

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField()
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey

    class Meta:
        app_label = 'api'

    def __str__(self):
        return self.name