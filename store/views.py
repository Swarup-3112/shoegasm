from typing import Counter
from django.shortcuts import render , redirect , get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .forms import createuserform 
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required 
from .models import cart
from .forms import addtocart

# Create your views here.



def home(request):
    form = UserCreationForm()
    context = {'form':form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request , username=username , password=password )   

        if user is not None:
            login(request, user)
            return redirect('store')  
        else:
            messages.info(request , 'username or password is incorrect ') 
            return render(request, 'home1.html' , context)         

    return render(request, 'home1.html' , context)

def logoutpage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='home') 
def store(request):
    products = product.objects.all().order_by('-id')[:4]
    casual = product.objects.filter(category ="Casual").order_by('-id')[:4]
    sport = product.objects.filter(category ="Sport").order_by('-id')[:4]
    sneaker = product.objects.filter(category ="Sneaker").order_by('-id')[:4]
    return render(request, 'store.html' , {'products':products, 'casual':casual , 'sport':sport ,'sneaker':sneaker})  

def addtocarts(request , id):
    prod = product.objects.get(name = id)    
    user = User.objects.get(username = request.user)
    c = cart()
    

    print(prod)
    print(user)
    


    c.customer = user
    c.product_id = prod
    # print(c)
    c.save()

    print( request.user )
    
    profile = product.objects.get(name = id)
    # print('profile :' + profile)
    return render(request, 'shoe_profile.html' ,{'profile':profile})

def shoeprofile(request , id):

    # prod = product.objects.get(name = id)    
    # user = User.objects.get( username = request.user)
    # c = cart()
    
    # c.customer = user
    # c.product_id = prod
    # c.save()
    # if request.method == 'POST':
    #     form = addtocart(request.POST)
    #     if form.is_valid():
    #         form.save()
          
        # post = cart
        # post.customer = request.POST.get('user')
        # post.product_id = request.POST.get('product')
        # post.save()
        
    #   product_id = request.POST.get('profile.id')
    #   user = request.POST.get('request.user')
    profile = product.objects.get(name = id)
    print(profile)
    return render(request, 'shoe_profile.html' ,{'profile':profile})

@login_required(login_url='home')
def menstoresport(request):
    menproduct = product.objects.filter(category="Sport").exclude(gender="Woman").order_by('-id')
    category = product.objects.get(id="1")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category}) 

@login_required(login_url='home')
def menstoresneaker(request):
    menproduct = product.objects.filter(category="Sneaker").exclude(gender="Woman").order_by('-id')
    category = product.objects.get(id="4")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category}) 

@login_required(login_url='home')
def menstorecasual(request):
    menproduct = product.objects.filter(category="Casual").exclude(gender="Woman").order_by('-id')
    category = product.objects.get(id="1")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category})       

@login_required(login_url='home')
def womenstoresport(request):
    menproduct = product.objects.filter(category="Sport").exclude(gender="Men").order_by('-id')
    category = product.objects.get(id="9")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category}) 

@login_required(login_url='home')
def womenstoresneaker(request):
    menproduct = product.objects.filter(category="Sneaker").exclude(gender="Men").order_by('-id')
    category = product.objects.get(id="4")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category}) 

@login_required(login_url='home')
def womenstorecasual(request):
    menproduct = product.objects.filter(category="Casual").exclude(gender="Men").order_by('-id')
    category = product.objects.get(id="8")
    return render(request, 'men-sports.html' ,{'menproduct':menproduct , 'Category':category})  

@login_required(login_url='home')
def carts(request):
    
    tax=0
    prod = cart.objects.filter(customer = request.user)
    subtotal = 0
    for prods in prod:   
      subtotal += prods.product_id.price 

    tax = subtotal * 0.02
    total = tax + subtotal
    
   
    return render(request , 'cart.html' , {'prod':prod , 'total':total , 'tax':tax , 'subtotal':subtotal} )

def deletes(request):
    
    prod = cart.objects.filter(customer = request.user)

    obj = get_object_or_404( product , id=id)
    if request.method == 'POST':
        obj.delete()     


    tax=0
    subtotal = 0
    for prods in prod:  
      subtotal += prods.product_id.price 

    tax = subtotal * 0.02
    total = tax + subtotal
    
   
    return render(request , 'cart.html' , {'prod':prod , 'total':total , 'tax':tax , 'subtotal':subtotal} )


