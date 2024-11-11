from django.db import models
from django.contrib import admin
class Bank_loan(models.Model):
   Name=models.CharField(max_length=20)
   Aadharno=models.IntegerField(primary_key="Aadharno")
   DoB=models.DateField()
   Address=models.CharField(max_length=20)
   Email=models.EmailField()
class Bank_loanAdmin(admin.ModelAdmin):
    list_display=('Name','Aadharno','DoB','Address','Email')