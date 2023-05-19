from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=30, primary_key=True)
    Principal=models.CharField(max_length=30)
    Location=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    school=models.ForeignKey(School, on_delete=models.CASCADE, related_name='Student')
    Sname= models.CharField(max_length=30)
    Sage=models.IntegerField()

    def __str__(self):
        return self.Sname
