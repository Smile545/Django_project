from django.shortcuts import redirect, render
from .models import Users, Article
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def indexpage(request):
    return render(request, 'index.html' )

@login_required
def aboutpage(request):
    return render(request, 'about.html')

@login_required
def contacnpage(request):
    if request.method == "GET":
        return render(request, 'contact.html', {"page": "contact"})
    else:
        print(request.POST)
        us = Users(
            name = request.POST['fname'],
            family = request.POST['lname'],
            email =  request.POST['email'],
            subject =  request.POST['subject'],
            message =  request.POST['message'],
        )
        us.save()
        return redirect(contacnpage)
    
@login_required    
def servicespage(request):
    return render(request, 'services.html')

@login_required
def workpage(request):
    return render(request, 'work.html')

@login_required
def blogpage(request):
    article = Article.objects.all()
    return render(request, 'blog.html', {'article': article})

@login_required
def flaskpage(request):
    return render(request, 'flask.html')


def sign_in(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        
        form = LoginForm()
        return render(request,'login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('index')
        
        # either form not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})
    
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')        