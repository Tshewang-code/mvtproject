from django.shortcuts import render
#import the model file in order to store data
from mvtapp.models import Webdevelopment_Details 

# Create your views here.
def insert_operation(request):
	print("INSIDE INSERT OPERATION")

	student_data=Webdevelopment_Details.object.create(name="Tshering",did="Ds(20)20-11345",age=23,gender="female",phone_no=175353663);
	print(student_data)

	student_data.save()
	return render(request,'mvtapp/display.html')
