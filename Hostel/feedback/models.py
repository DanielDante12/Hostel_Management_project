from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    Rating=models.DecimalField()
    comment=models.CharField(max_length=200)
    Date=models.DateField()
    Student=models.ForeignKey(User,on_delete=models.CASCADE)

class Hostel(models.Model):
    Address=models.CharField()
    Telno=models.CharField(max_length=15)
    Email=models.CharField()
    status=models.CharField()
    Image=models.ImageField(upload_to='static/hostel')
    manager=models.ForeignKey(User, on_delete=models.CASCADE)

class Payment(models.Model):
    Amount=models.DecimalField()
    PaymentDate=models.DateField()
    PaymentMethod=models.CharField()
    
class Reservation(models.Model):
    CheckInDate=models.DateField()
    CheckOutDate=models.DateField()
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment, on_delete=models.CASCADE)

class Room(models.Model):
    Room_number=models.CharField()
    Room_type=models.CharField()
    status=models.CharField()
    Hostel=models.ForeignKey(Hostel, on_delete=models.CASCADE)
    Reservation=models.ForeignKey(User,null=True,blank=True)



# Create your models here.
