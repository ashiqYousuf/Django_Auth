from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm , LoginForm , PostForm
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request , 'blog/home.html',{'posts':posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request , 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        full_name=request.user.get_full_name()
        gps=request.user.groups.all()
        return render(request , 'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request , user)
                    messages.success(request , 'Logged In Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=LoginForm()
        return render(request , 'blog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_signup(request):
    if request.method=="POST":
        fm=SignUpForm(data=request.POST)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request , 'Account Created Successfully')
            fm=SignUpForm()
    else:
        fm=SignUpForm()
    return render(request , 'blog/signup.html',{'form':fm})
    
def addpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PostForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request , 'Post Created Successfully')
                return HttpResponseRedirect('/dashboard/addpost/')
        else:
            fm=PostForm()
        return render(request , 'blog/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            fm=PostForm(request.POST , instance=pi)
            if fm.is_valid():
                fm.save()
                messages.info(request , 'Post Updated Successfully')
        else:
            pi=Post.objects.get(pk=id)
            fm=PostForm(instance=pi)
        return render(request , 'blog/updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')