from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'index.html', context)

def doctors(request):
    context = {}
    return render(request, 'doctor.html', context)

def services(request):
    context = {}
    return render(request, 'services.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)
