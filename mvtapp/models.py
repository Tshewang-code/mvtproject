from django.db import models

# Create your models here.
class Webdevelopment_Details(models.Model):
	did=models.CharField(primary_key=True,max_length=50)
	name=models.CharField(max_length=20)
	age=models.IntegerField()
	phone_no=models.BigIntegerField(unique=True)
	gender=models.CharField(max_length=50)

	class Meta:
		verbose_name="Webdevelopment_Details"
		verbose_name_plural="Webdevelopment_Detailss"
	def __str__(self):
		return self.name

