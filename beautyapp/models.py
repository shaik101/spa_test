from django.db import models

# Create your models here.

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

def __str__(self):
    return self.firstame

class Citys(models.Model):
        name=models.CharField(max_length=50,default="delhi")

        def __str__(self):
            return self.name

class Services(models.Model):
        name=models.CharField(max_length=50,default="leg")



        def __str__(self):
            return self.name


class Gift(models.Model):
        name=models.CharField(max_length=50)
        email=models.CharField(max_length=50)
        mobile=models.IntegerField()
        address=models.CharField(max_length=200)
        message=models.CharField(max_length=500)
        price=models.IntegerField()


        def __str__(self):
            return self.name



class Appointment(models.Model):
    name=models.CharField(max_length=50)
    mobileno = models.IntegerField()
    city = models.ForeignKey(Citys, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    services = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Carriers(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    date=models.DateField()
    email=models.CharField(max_length=100)
    mobileno = models.IntegerField()
    totalexp=models.CharField(max_length=100)
    lastsalary=models.IntegerField()
    fileupload=models.FileField(upload_to='beautyapp/Resume')
    def __str__(self):
        return self.name
