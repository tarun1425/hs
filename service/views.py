from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from service.models import Have_Flat , Need_Flat
# Create your views here.


def services(request):
    return render(request,'service/services.html')

def haveFlatForm(request):
    try:
        print('session is still working : '+request.session['sessionId'])
        logReq = ''
    except:
        print('login required')
        logReq = 'login required'
        #return render(request,'service/pages/haveFlatForm.html',{'logReq': 'Login Required' }
        
        
    heading = 'Have Flat'
    headingTitle = 'Looking for roommate'
    
    if request.method == 'POST':
        
        _location = request.POST['location']
        _city = request.POST['city']
        _state = request.POST['state']
        _rent = request.POST['rent']
        try:
            _email = request.session['sessionId']
        except:
            return render(request,'service/pages/haveFlatForm.html',{'heading':heading,'headingTitle':headingTitle,'logReq':logReq})
        
        
        _haveFlat = Have_Flat(location = _location, city = _city, state = _state, rent = _rent , email = _email)
        _haveFlat.save()
        print('have flat form submited')
        return redirect('/',)
    
    else:
        return render(request,'service/pages/haveFlatForm.html',{'heading':heading,'headingTitle':headingTitle,'logReq':logReq})


def needFlatForm(request):
    try:
        print('session is still working : '+request.session['sessionId'])
        logReq = ''
    except:
        print('login required')
        logReq = 'login required'
        #return render(request,'service/pages/haveFlatForm.html',{'logReq': 'Login Required' }
        
        
    heading = 'Need Flat'
    headingTitle = 'Looking for room'
    
    if request.method == 'POST':
        
        _location1 = request.POST['location1']
        _location2 = request.POST['location2']
        _city = request.POST['city']
        _state = request.POST['state']
        _rent = request.POST['rent']
        try:
            _email = request.session['sessionId']
        except:
            return render(request,'service/pages/needFlatForm.html',{'heading':heading,'headingTitle':headingTitle,'logReq':logReq})
        
        
        _needFlat = Need_Flat(location_1 = _location1, location_2 = _location2, city = _city, state = _state, rent = _rent , email = _email)
        _needFlat.save()
        print('need flat form submited')
        return redirect('/',)
    
    else:
        return render(request,'service/pages/needFlatForm.html',{'heading':heading,'headingTitle':headingTitle,'logReq':logReq})
