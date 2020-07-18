from django.db import models


class AddClassModel(models.Model):
    Idno=models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20,unique=True)
    Faculty = models.CharField(max_length=20)
    Date = models.DateField()
    Time = models.TimeField()
    Fee = models.FloatField()
    Duration = models.IntegerField()


class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    Contactno = models.IntegerField(primary_key=True,unique=True)
    emailid = models.EmailField(unique=True)
    password= models.CharField(max_length=20)

class EnroleListModel(models.Model):
    Contanctno=models.ForeignKey(StudentModel,on_delete=models.CASCADE)
    idno=models.ForeignKey(AddClassModel,on_delete=models.CASCADE)
