from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from account.models import Registration
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# ----------------------REGISTRATION----------------------

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        user = User.objects.create_user(username=email, email= email, password=password1, first_name= first_name, last_name= last_name)
        registration = Registration(first_name =first_name, last_name= last_name,email = email, phone = phone_number, password = password1)
        
        user.save()        
        registration.save()
        
        print('user created')
        return redirect('/')
    else:
        return render(request,'account/register.html')



# ----------------------LOGIN----------------------

def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # authentication management
        user = authenticate(username = username, password =password)
        login(request,user)
        print('login successfully')
        
        # session management
        if user is not None:
            request.session['sessionId'] = user.username
            request.session.set_expiry(300) # 5*60 = 300 seconds
            print('session start : '+request.session['sessionId'])
            return redirect('/')
    else:
        return render(request,'account/signin.html')


# ----------------------SIGNOUT----------------------
def signout(request):
    
    # session managment
    print('session close :')
    try:
        del request.session['sessionId']
    except:
        pass
    
    # de-auth managment
    auth.logout(request)
    print('sign out successfully')
    
    return redirect('/')