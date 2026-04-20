from django.shortcuts import render
from plants.models import Plant
from django.shortcuts import render, redirect
from plants.models import Contact
 


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
    if request.method == 'POST':
        Contact.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        return redirect('/messages/')

    return render(request, 'core/contact.html')


def messages_view(request):
    messages = Contact.objects.all().order_by('-created_at')

    return render(request, 'core/messages.html', {
        'messages': messages
    })
