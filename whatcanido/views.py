from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from .forms import DataForm
from .models import Data

# Create your views here.
def home(request):
    return render(request, 'whatcanido/index.html', {})

def donate(request):
    return render(request, 'whatcanido/donate.html', {})

def contribute(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('/submitted/')
    form = DataForm()

    return render(request,'whatcanido/contribute.html', {'form':form})

def submitted(request):
    return render(request, 'whatcanido/submitted.html', {})

def problemlist(request, category_slug=None):
    if category_slug:
        t = category_slug
        qs = Data.objects.filter(category__category_slug = t)
    else:
        t = request.GET.get('querry')
        qs = Data.objects.filter(name__icontains=t)
    return render(request, 'whatcanido/list.html', {'qs':qs, 't':t})

def problem(request, problem_slug):
    qs = Data.objects.get(name_slug =problem_slug)
    return render(request, 'whatcanido/problem.html', {'qs':qs})

    