from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    #return HttpResponse("<h1>Hello, World!</h1><h3>Thursday</h3>")
    return render(request, 'generator/home.html', {'password': '1234'})

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12)) #12 is the default value
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!"£$%^&*()_+-?><@#'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    for x in range(length):
        thepassword += random.choice(characters)
        
    return render(request,'generator/password.html', {'password': thepassword })

def about(request):
    return render(request, 'generator/about.html')