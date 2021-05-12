from django.shortcuts import render,redirect
from djanpost.forms import LogInForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from djanpost.models import LogIn
# Create your views here.

def home(request):
    return render(request,"index.html")  

def login(request):
    form=LogInForm()
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        if LogIn.objects.filter(username=username, password=password).exists():
            log=LogIn.objects.get(username=username, password=password)
            return redirect('/home/')
        else:
            msg='invalid Username or Password'
            return render(request,"login.html",{'err':msg,'form':form})
    return render(request,"login.html",{'form':form})

def register(request):
    if request.method == "POST":
       form=LogInForm(request.POST)
       if form.is_valid():
            try:
               form.save()
               return redirect('/home/')
            except:
                pass
    else:
        form=LogInForm()
        return render(request,"register.html",{'form':form})


