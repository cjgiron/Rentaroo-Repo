from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect

from .forms import CityForm


def index(request):
    return render(request, "home.html")

def thanks(request):
    return render(request, "thanks.html")


def get_city(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CityForm()
        context = {
            'form': form
        }

    return render(request, 'home.html', context)