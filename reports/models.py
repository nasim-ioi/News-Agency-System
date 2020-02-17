from django.db import models

# Create your models here.

class ReportersTable(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class ReportsTable(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateField()
    reporter = models.ForeignKey(ReportersTable , on_delete=models.CASCADE)

    def __str__(self):
        return "khabar"
    

