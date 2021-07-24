from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Apartment, User
import bcrypt
from .forms import ApartmentForm


def index(request):
    return render(request, "index.html")

def thanks(request):
    return render(request, "thanks.html")


def home(request):
    if "user_id" not in request.session:
        return redirect('/')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ApartmentForm(request.POST)
        # check whether it's valid:

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ApartmentForm()

    return render(request, 'home.html', {'form': form})

def create_listing(request):

    
    Apartment.objects.create(
        city = request.POST['city'],
        street_address = request.POST['street_address'],
        apartment_img = request.POST['apartment_img'],
        monthly_rent = request.POST['monthly_rent'],
        renovated = True if request.POST.get('renovated') else False,
        air_conditioning = True if request.POST.get('air_conditioning') else False,
        pool = True if request.POST.get('pool') else False,
        allows_pets = True if request.POST.get('allows_pets') else False,
        laundry_onsite = True if request.POST.get('laundry_onsite') else False
    )
    
    return redirect('/all_apartments')


def login_process(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/home')


def register_process(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        print(pw_hash)

        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )
        
        request.session['user_id'] = user.id

        return redirect('/home')


def all_apartments(request):
    apartments = Apartment.objects.all()

    context = {
        'apartments': apartments
    }
    return render(request, 'all_apartments.html', context)

def search_cities(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        apartments = Apartment.objects.filter(city__contains=searched)
        return render(request, "search_cities.html", {'searched': searched, 'apartments': apartments})
    else:
        return redirect('/home')

def logout(request):
    request.session.flush()
    return redirect('/')