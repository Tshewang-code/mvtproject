from django.shortcuts import render
from formapp.models import FromDetails
from formapp.forms import FromDetailsForm

# Create your views here.
def form_display(request):
	if request.method=='GET':
		#Creating the object of the form for displaying for displaying the form on the web browser
		form=FromDetailsForm()
		return render(request,'formapp/display.html',context={"form":form})

def form_accept(request):
	if request.method=='POST':
		#Fetching the data from the web browser using .POST
		form=FromDetailsForm(request.POST)
		if form.is_valid():
			form.save()
	form=FromDetailsForm()
	return render(request,'formapp/display.html',context={"form":form})

