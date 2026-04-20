from django.shortcuts import render
from plants.models import Plant
from django.shortcuts import render, redirect
from .models import Contact
 


# Create your views here.

def home_view(request):
    return render(request, 'core/home.html')

def contact_view(request):
    return render(request, 'core/contact.html')



def home(request):

    plants = Plant.objects.all()[:3]  

    return render(request, 'core/home.html', {
        'plants': plants
    })



def contact(request):
    errors = []
    form_data = {}

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'message': message,
        }

        if not first_name:
            errors.append('First name is required')
        if not last_name:
            errors.append('Last name is required')
        if not email or '@' not in email:
            errors.append('Valid email is required')
        if not message:
            errors.append('Message is required')

        if not errors:
            Contact.objects.create(**form_data)
            return redirect('/contact/?sent=1')

    return render(request, 'core/contact.html', {
        'errors': errors,
        'form_data': form_data,
    })

def messages_view(request):
    contacts = Contact.objects.all().order_by('-created_at')

    return render(request, 'core/messages.html', {
        'contacts': contacts
    })