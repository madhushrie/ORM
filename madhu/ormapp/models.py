from django.db import models
from django.contrib import admin 
class bankloan(models.Model):
	name=models.CharField(max_length=15)
	phoneno=models.IntegerField()
	accountno=models.IntegerField(primary_key="accountno")
	loan_amount=models.IntegerField()
	interset=models.FloatField()
class bankloanadmin(admin.ModelAdmin):
	list_display=('name','phoneno','accountno','loan_amount','interset')
