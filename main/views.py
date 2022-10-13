from django.shortcuts import render, redirect
from .models import Cars, Drivers
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
# Create your views here.
@login_required(login_url='login_page')
def base(request):
    return render(request, "base.html")

@login_required(login_url='login_page')
def cars(request):
    user = request.user
    db = Cars.objects.filter(user=user)

    return render(request, 'cars.html', {'db':db})

@login_required(login_url='login_page')
def add_cars(request):

    if request.method == "POST":
        user = request.user
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        color = request.POST.get("color")
        number = request.POST.get("number")
        cars  = Cars.objects.create(brand=brand, model=model, color=color, number=number, user=user)
        return redirect("cars")
    return render(request, "add_cars.html")

@login_required(login_url='login_page')
def edit_cars(request, pk):
    if request.method == "POST":
        
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        color = request.POST.get("color")
        number = request.POST.get("number")
        
        
        db = Cars.objects.get(id=pk)
        
        
        db.brand = brand
        db.model = model
        db.color = color
        db.number = number
        db.save()
       
        return redirect("cars")
        
        
    if request.method == "GET":
        db = Cars.objects.get(id=pk)
        context = {"db": db}
        return render(request, "edit_cars.html", context=context)

@login_required(login_url='login_page')
def view_cars(request, pk):
     if request.method == "GET":
        car = Cars.objects.get(id=pk)
        driver = Drivers.objects.filter(car=car)
        context = {"car": car, "driver":driver}
        return render(request, "info_cars.html", context=context)

@login_required(login_url='login_page')    
def delete_cars(request, pk):
    if request.method == "POST":
        db = Cars.objects.get(id=pk)
        db.delete()
        return redirect("cars")
    if request.method == "GET":
        db = Cars.objects.get(id=pk)
        context = {"db": db}
        return render(request, "delete_cars.html", context=context)

@login_required(login_url='login_page')
def drivers(request):
    user = request.user
    db = Drivers.objects.filter(user=user)
    return render(request, 'drivers.html', {'db':db})

@login_required(login_url='login_page')
def add_drivers(request):
    user = request.user
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        car = int(request.POST.get('car'))
        car_itself = Cars.objects.get(id=car)
        driver  =Drivers.objects.create(first_name=first_name, last_name=last_name, car = car_itself, user=user)
        print(driver)    
        
        return redirect("cars")
    db = Cars.objects.filter(user=user)

    return render(request, "add_drivers.html", {'db':db})

@login_required(login_url='login_page')
def delete_drivers(request, pk):
    if request.method == "POST":
        db = Drivers.objects.get(id=pk)
        db.delete()
        return redirect("cars")
    if request.method == "GET":
        db = Drivers.objects.get(id=pk)
        context = {"db": db}
        return render(request, "delete_drivers.html", context=context)
    pass

@login_required(login_url='login_page')
def edit_drivers(request, pk):
    if request.method == "POST":
        
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
    
        
        db = Drivers.objects.get(id=pk)
        
        
        db.first_name = first_name
        db.last_name = last_name

        db.save()
      
       
        return redirect("drivers")
        
        
    if request.method == "GET":
        db = Drivers.objects.get(id=pk)
        context = {"db": db}
        return render(request, "edit_drivers.html", context=context)


def register_page(request):
    page = 'register'
    form = RegistrationForm()
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('cars')
    return render(request, 'register_page.html', {'form':form, 'page':page})

def login_page(request):
    page = 'login'
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars')
        else:
            return render(request, 'login_page.html')

            
    return render(request, 'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')