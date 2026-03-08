from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'main/login.html', context)
    return render(request, 'main/login.html')

def home(request):
    context = {
        'message': 'Welcome to the Home Page!',
    }
    return render(request, 'main/home.html', context)

def resources(request):
    context = {
        'resources': [
            'Django Documentation',
            'Django Tutorials',
            'Django Community',
        ],
    }
    return render(request, 'main/resources.html', context)
def pricing(request):
    context = {
        'plans': [
            {'name': 'Basic', 'price': '$10/month'},
            {'name': 'Pro', 'price': '$20/month'},
            {'name': 'Enterprise', 'price': '$50/month'},
        ],
    }
    return render(request, 'main/pricing.html', context)

@login_required(login_url='login')
def profile(request):
    with open("login_times.log", "r") as f:
        login_times = f.read() 

    char_list = list(login_times) 

    time_list = char_list[0:10] 
    ip_list = char_list[42:51]
    time_login = ' '.join([str(element) for element in time_list]) 

    user_ip = ' '.join([str(element) for element in ip_list]) 
    context = {
        'user': request.user,
        # 'char_list': char_list,
        'login_time': str(time_login),
        'user_ip': str(user_ip),
    }
    return render(request, 'main/profile.html', context)