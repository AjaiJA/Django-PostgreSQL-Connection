from django.db import models

# Create your models here.

class LogIn(models.Model):  
    username = models.EmailField()
    password = models.CharField(max_length=10)  
    class Meta:  
        db_table = "useracc"  