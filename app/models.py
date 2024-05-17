from django.db import models

# Create your models here.

class Topic(models.Model):
    Topic_Name=models.CharField(primary_key=True,max_length=100)

    def __str__(self):
        return self.Topic_Name


class Webpage(models.Model):
    Topic_Name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    URL=models.URLField()

    def __str__(self):
        return self.Name


class AccessRecord(models.Model):
    Name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    Date=models.DateField()
    Author=models.CharField(max_length=100)

    def __str__(self):
        return self.Author