from django.shortcuts import render
from .models import Contact
def index(request):
    return render(request, 'index.html', {})

def AboutUs(request):
    return render(request, 'AboutUs.html', {})
def Menu(request):
    return render(request,'Menu.html',{})
def Features(request):
    return render(request,'Features.html',{})
def Catering(request):
    return render(request,'Catering.html',{})
def ContactUs(request):
    
        return render(request,'ContactUs.html',{})
def submit_contact_view(request):
    if request.method =="POST":
         name =request.POST.get('name')
         email =request.POST.get('email')
         message=request.POST.get('message')
         contact =Contact.objects.create(name=name,email=email,message=message)
         contact.save()
         return render(request, 'succes.html', {'success_message': 'Message submitted successfully!'})
    else:
       
        return render('index.html')