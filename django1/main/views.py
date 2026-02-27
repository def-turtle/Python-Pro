from django.shortcuts import render

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

def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'main/profile.html', context)