from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):	
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name','autocomplete':'off'}))
	people = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'no of people','autocomplete':'off'}))
	date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class':'form-control','placeholder':'DateTime','autocomplete':'off'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message','autocomplete':'off'}))

	class Meta:
		model = Contact
		fields = ['name','people','date','message']