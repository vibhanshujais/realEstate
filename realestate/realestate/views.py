from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.core.cache import cache
from realstates.models import user, query, property_booking_details
def home(request):
    """ if request.user.is_authenticated:
        return render(request, 'home.html', {'name':request.user.email})
    else:
        return render(request, 'home.html') """
    value = cache.get('name')
    return render(request, 'home.html',{'name':value})


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
        data['email'] = i.email
        data['no'] = i.number
    if data:
        cache.set('name', data['name'], timeout=3600)
        cache.set('email',data['email'], timeout=3600)
        cache.set('no',data['no'], timeout=3600)
    return redirect('/')

def logout(request):
    cache.delete('name')
    cache.delete('email')
    cache.delete('no')
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
    value = cache.get('name')
    return render(request, 'flat.html', {'name' : value})

def fh(request):
    value = cache.get('name')
    return render(request, 'fh.html', {'name':value})

def plot(request):
    value = cache.get('name')
    return render(request, 'plot.html', {'name':value})

def userdashboard(request):
    name = cache.get('name')
    email =  cache.get('email')
    ob = property_booking_details.objects.filter(user=name, email=email)
    data={'key':ob}
    print(ob)
    l=[]
    for i in data['key']:
        if i not in l:
            l.append((i))
            
    print(l)
    return render(request, 'userdashboard.html',{'name':name,'email':email,'key':l})

def querymodel(request):
    name = request.POST.get('fn') + request.POST.get('ln')
    email = request.POST.get('email')
    description = request.POST.get('description')
    ob = query(name=name,email=email,description=description)
    ob.save()
    return redirect('/')

def f1(request):
    return render(request, 'f1.html')

def f2(request):
    return render(request, 'f2.html')
def fbook(request):
    id = request.POST.get('id')
    no = cache.get('no')
    email = cache.get('email')
    category = 'flat'
    name = cache.get('name')
    if name:
        ob = property_booking_details(user=name,number=no,email=email,category=category,p_id=id)
        ob.save()
        return redirect('/flat')
    else:
        return redirect('/login')