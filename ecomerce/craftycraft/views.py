from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
    return render(request,"craft/homepage.html")
def login(request):
    if request.method=="post":
        username=request.post['username']
        pass1=request.post['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"craft/register.html",{"fname":fname})
        else:
            messages.error(request,"Bad Credentials!") 
            return redirect('homepage')   
    return render(request,"craft/login.html")
def register(request):
    if request.method =="post":
        username=request.post['username']
        fname=request.post['fname']
        lname=request.post['lname']
        email=request.post['email']
        pass1=request.post['pass1']
        pass2=request.post['pass2']
         
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"Your account has successfuly created") 
        return redirect('login')
    return render(request,"craft/register.html")    
def products(request):
    return render(request,"craft/products.html")
def contact(request):
    return render(request,"craft/contact.html")    
# def homepage(request):
#     return render(request,"craft/homepage.html")

