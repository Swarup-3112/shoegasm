from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home1(request):
    return render(request, 'home1.html')
    
def home(request):
    return render(request, 'home.html')

def store(request):
    products = product.objects.all().order_by('-id')[:4]
    casual = product.objects.filter(category ="Casual").order_by('-id')[:4]
    sport = product.objects.filter(category ="Sport").order_by('-id')[:4]
    sneaker = product.objects.filter(category ="Sneaker").order_by('-id')[:4]
    return render(request, 'store.html' , {'products':products, 'casual':casual , 'sport':sport ,'sneaker':sneaker})  

def shoeprofile(request , id):
    profile = product.objects.get(name = id)
    return render(request, 'shoe_profile.html' ,{'profile':profile})

def menstoresport(request):
    menproduct = product.objects.filter(category="Sport").exclude(gender="Woman").order_by('-id')
    category = product.objects.get(id="1")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category}) 

def menstoresneaker(request):
    menproduct = product.objects.filter(category="Sneaker").exclude(gender="Woman").order_by('-id')
    category = product.objects.get(id="4")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category}) 

def menstorecasual(request):
    menproduct = product.objects.filter(category="Casual").exclude(gender="Woman").order_by('-id')
    category = product.objects.get(id="1")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category})       

def womenstoresport(request):
    menproduct = product.objects.filter(category="Sport").exclude(gender="Men").order_by('-id')
    category = product.objects.get(id="8")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category}) 

def womenstoresneaker(request):
    menproduct = product.objects.filter(category="Sneaker").exclude(gender="Men").order_by('-id')
    category = product.objects.get(id="4")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category}) 

def womenstorecasual(request):
    menproduct = product.objects.filter(category="Casual").exclude(gender="Men").order_by('-id')
    category = product.objects.get(id="1")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category})  