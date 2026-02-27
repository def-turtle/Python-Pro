from django.shortcuts import render

def index(request):
    return render(request, 'base/index.html')

def features(request):
    return render(request, 'base/features.html')