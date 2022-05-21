from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello..........")

def special(request):
    
    return render(request,'store/special.html')