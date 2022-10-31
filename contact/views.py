from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def contact_view(request):
	if request.method == "POST":
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			contact_form.save()
			messages.success(request, ('Your movie was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
		
		
		return redirect("home")
	contact_form = ContactForm()
	contacts = Contact.objects.all()
	return render(request=request, template_name="contact/contact.html", context={'contact_form': contact_form, 'contacts': contacts})