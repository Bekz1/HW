from django.shortcuts import render, redirect
from .models import Cars, Drivers
# Create your views here.

def base(request):
    return render(request, "base.html")

def cars(request):
    db = Cars.objects.all()

    return render(request, 'cars.html', {'db':db})

def add_cars(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        color = request.POST.get("color")
        number = request.POST.get("number")
        cars  = Cars.objects.create(brand=brand, model=model, color=color, number=number)
        return redirect("cars")
    return render(request, "add_cars.html")
    
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
def view_cars(request, pk):
     if request.method == "GET":
        car = Cars.objects.get(id=pk)
        driver = Drivers.objects.filter(car=car)
        context = {"car": car, "driver":driver}
        return render(request, "info_cars.html", context=context)
    

    
def delete_cars(request, pk):
    if request.method == "POST":
        db = Cars.objects.get(id=pk)
        db.delete()
        return redirect("cars")
    if request.method == "GET":
        db = Cars.objects.get(id=pk)
        context = {"db": db}
        return render(request, "delete_cars.html", context=context)

def drivers(request):
    db = Drivers.objects.all()
    return render(request, 'drivers.html', {'db':db})

def add_drivers(request):
   
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        car = int(request.POST.get('car'))
        driver  =Drivers.objects.create(first_name=first_name, last_name=last_name, car = car)
        print(driver)    
        
        return redirect("cars")
    db = Cars.objects.all()

    return render(request, "add_drivers.html", {'db':db})


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

