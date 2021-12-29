from django import forms
from formapp.models import FromDetails

class FromDetailsForm(forms.ModelForm):
	class Meta:
		model=FromDetails
		fields='__all__'