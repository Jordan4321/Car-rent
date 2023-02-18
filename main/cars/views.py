from django.shortcuts import render
from .models import Car
from .forms import OrderForm
from django.http import HttpResponseRedirect


def cars(request):
    cars = Car.objects.all()

    return render(
        request,
        'cars/cars.html',
        context={'cars': cars}
    )


def info_car(request, id):
    obj = Car.objects.get(id=id)
    context = {
        'car': obj
    }

    return render(request, 'cars/info_car.html', context=context)


def order_car(request):
    submitted = False
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('/cars/order_car?submitted=True')
    else:
        form = OrderForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'cars/order_car.html', {'form': form, 'submitted': submitted})


def rent(request):
    return render(request, 'cars/rent.html')

