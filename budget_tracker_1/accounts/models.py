from django.db import models

# Create your models here.

class Ind_User(models.Model):
    username = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
    e_file = models.FileField(upload_to='uploads/', default='Ind_User_Data.xlsx')
