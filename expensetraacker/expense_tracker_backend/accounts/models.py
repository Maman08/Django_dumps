from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class CustomUser(AbstractUser):
    email=models.EmailField(max_length=30,unique=True)
    username=models.CharField(max_length=150,unique=True,default="default_user")
    phone=models.CharField(max_length=13)
    otp=models.CharField(max_length=6)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return f"{self.email} - {self.phone}"
    


#     Ab __str__ method ka kaam ye hota hai ki jab bhi tu kisi CustomUser object ko print kare (print(user)) ya Django admin panel me dekhe, to kya dikhna chahiye.

# Tu __str__ me return self.email likh raha hai, iska matlab hai ki jab bhi tu CustomUser ka object print karega, wo uska email return karega

