from django.shortcuts import render, redirect , HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import *





def user_Login(request):
    if request.method == 'GET':
        context = {}
        context['form'] = AuthenticationForm()
        return render(request, 'user_account/login.html', context)

    elif request.method == 'POST':
        lf = AuthenticationForm(data=request.POST)
        if lf.is_valid():
            username = lf.cleaned_data.get('username')
            password = lf.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            login(request,user)
    
            if user.is_superuser==True:
                return redirect('adminhome')
                
            elif user.is_staff==True:
                return redirect('staff_home')
            
            elif user:
                return redirect('homepage')

        else:
            messages.info(request,"Invalide Username Or Password")
            context = {}
            context['form'] = lf
            return render(request, 'user_account/login.html', context)


def user_Register(request):
    if request.method == 'GET':
        context = {}
        context['forms'] = RegisterForm()
        return render(request, 'user_account/register.html', context)

    elif request.method == 'POST':
        rf = RegisterForm(request.POST or None)
        if rf.is_valid():
            user=rf.save(commit=False)
            user.set_password(rf.cleaned_data.get('password'))
            user.is_student=0
            user.save()
            return redirect('loginpage')
        else:
            print(rf.errors)
            context = {}
            context['forms'] = rf
            return render(request, 'user_account/register.html', context)



def user_logout(request):
    logout(request)
    return redirect('homepage')




