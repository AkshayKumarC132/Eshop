import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Extending User Model as User_Profile and Some more fields 
class User_profile(AbstractUser):
    id = models.AutoField(primary_key=True,db_column='user_id')  
    username = models.CharField(max_length=100,unique=True) 
    first_name=models.CharField(max_length=250) 
    last_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250, unique=True) 
    mobile=models.CharField(max_length=15, unique=True)
    age=models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    created_date =models.DateTimeField(default=datetime.datetime.now())
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # str function in a django model returns a string that is exactly rendered as the display name of instances for that model.
    def __str__(self):
        self.username

    
