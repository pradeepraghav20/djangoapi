from django.db import models

# Create your models here.
class Company (models.Model):
    company_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('NON-IT','NOT-IT'),('MOBILE PHONE','MOBILE PHONE')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=50)
    about=models.TextField()
    position=models.CharField(max_length=100,choices=(('manager','manager'),('TL','TL'),('Senior manger','Senior manger')))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    







    

