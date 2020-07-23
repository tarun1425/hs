from django.shortcuts import render,redirect
from contact.models import Contect
# Create your views here.

def contact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        con = Contect(name = name, email = email, subject= subject, message = message)
        con.save()
    else:
        return render(request,'contact/contact.html')
    
    return render(request,'contact/contact.html')