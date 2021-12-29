from django.db import models

# Create your models here.
class FromDetails(models.Model):
	usn=models.CharField(primary_key=True,max_length=20)
	name=models.CharField(max_length=30)
	age=models.PositiveIntegerField()
	stream=models.CharField(max_length=30)
	section=models.CharField(max_length=10)

	class Meta:
		verbose_name="FromDetails"
		verbose_name_plural="FromDetailss"

	def __str__(self):
		return self.usn





