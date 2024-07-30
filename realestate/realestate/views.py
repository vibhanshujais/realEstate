from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.core.cache import cache
from realstates.models import user
def home(request):
    """ if request.user.is_authenticated:
        return render(request, 'home.html', {'name':request.user.email})
    else:
        return render(request, 'home.html') """
    value = cache.get('key')
    return render(request, 'home.html',{'key':value})


def login(request):
    try:
        name = request.POST.get('firstname') + request.POST.get('lastname')
        email = request.POST.get('email')
        number = request.POST.get('contact')
        password = request.POST.get('password')
        cpass = request.POST.get('cpassword')
        if password==cpass:
            ob = user(name = name, email = email, number = number, password = password)
            ob.save()
        else:
            return redirect('register/')
        return render(request, 'login.html')
    except:
        return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def dashboard(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    ob = user.objects.filter(email = email, password = password)
    data = {}
    for i in ob:
        data['name'] = i.name
    if data:
        cache.set('key', data['name'])
    return redirect('/')

def logout(request):
    cache.delete('key')
    return redirect('/')

""" 
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
 """


def flat(request):
    value = cache.get('key')
    return render(request, 'flat.html', {'key' : value})