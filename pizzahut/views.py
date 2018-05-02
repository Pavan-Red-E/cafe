from django.shortcuts import render, HttpResponse
from .forms import ContactForm





def Contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'siri.html',{'form':form})
		else:
			form = ContactForm()
	return render(request,'siri.html',{'form':form})


# Create your views here.
