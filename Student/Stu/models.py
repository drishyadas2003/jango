from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher=models.CharField(max_length=255)

    def __str__(self) :
        return self.teacher
    
class Batch(models.Model):
    batch=models.CharField(max_length=255)
    
    def __str__(self) :
        return self.batch
    
class Student(models.Model):
    name=models.CharField(max_length=255)
    age=models.CharField(max_length=100)
    contact=models.CharField(max_length=255)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)