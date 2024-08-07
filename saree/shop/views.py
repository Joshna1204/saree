from django.shortcuts import render,redirect
from shop.models import Category,Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def allproducts(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request,'products.html',{'c':c,'p':p})

def allcategories(request):
    c=Category.objects.all()
    p=Product.objects.all()
    return render(request,'category.html',{'c':c,'p':p})

def detail(request,p):
    product = Product.objects.get(name=p)
    return render(request, 'details.html', {'p': product})

def user_login(request):
    if (request.method == "POST"):
        name = request.POST['u']
        pas = request.POST['p']
        user=authenticate(username=name,password=pas)
        if user:
            login(request,user)
            return redirect('shop:allcategories')
        else:
            messages.error(request,'Invalid credentails')

    return render(request,'login.html')

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST['e']
        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e)
            u.save()
            return redirect('shop:allcategories')
        else:
            return HttpResponse("password not matching")
    return render(request,'register.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)

def about(request):
    c = Category.objects.all()
    p = Product.objects.all()
    return render(request, 'about.html', {'c': c, 'p': p})