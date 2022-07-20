from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'deepdive/index.html', {'form': form})

def index(request):
    return render(request, "deepdive/index.html",{})