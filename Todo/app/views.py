from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def Home(request):
    if request.method == 'POST':
        title=request.POST['title']
        detail=request.POST['detail']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        todo=Todo.objects.create(title=title,detail=detail,startdate=startdate,enddate=enddate)
        print(todo.title)
        todo.save()
        return redirect('listing')
    # todos=Todo.objects.all()
    return render(request,'home.html')

def List(request):
    todos=Todo.objects.all()
    return render(request,'list.html',{'todos':todos})


def Edit(request,id):
     edit=Todo.objects.get(id=id)
    
     if request.method == 'POST':   
        title=request.POST['title']
        detail=request.POST['detail']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        if edit:  
            edit.title=title
            edit.detail=detail
            edit.startdate=startdate
            edit.enddate=enddate
            edit.save()
     


        return redirect('listing')
     return render(request,'edit.html',{'edit':edit})


def remove(request,id):
    todo=Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')

def register(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        reg=User.objects.create_user(username=name,email=email,password=password)
        print(name,email,password)
        reg.save()
    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        print(name, password)
        #checking for user is valid
        if user is not None:
            login(request, user)
            print('success')
            return redirect('home')
        else:
            print('error')
            messages.error(request,'the user is not valid')
            return redirect('login')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def Calcu(request):
    result=''
    if request.method=='POST':
        a=int(request.POST.get('num1'))
        z=request.POST.get('operation')
        b=int(request.POST.get('num2'))
        
        if z=='+':
            result=a+b
        elif z=='-':
            result=a-b
        elif z=='/':
            result=a/b
        elif z=='*':
            result=a*b
        else:
            result='invalid operation'
        # print(result)
        return render(request,'calculator.html',{'result':result})
    return render(request,'calculator.html')
# Create your views here.
