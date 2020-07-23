from django.shortcuts import render,redirect
from django.http import HttpResponse
from service.models import Have_Flat, Need_Flat
# Create your views here.
def index(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/pages/about.html')

def searchLocation(request):
    context = {}
    
    if request.method == 'POST':
        _location = request.POST['searchLocation']
        
        context['citysHaveFlat'] = Have_Flat.objects.all().filter(city=_location)
        context['citysNeedFlat'] = Need_Flat.objects.all().filter(city=_location)
         
        return render(request,'home/searchResult.html',context)
