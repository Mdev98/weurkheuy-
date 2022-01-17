from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from urllib.parse import urlencode

from jobs.models import Job, JobForm
from jobs.forms import Apply

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            jobs = Job.objects.filter(name=name)
            return render(request, 'jobs/list_job.html', {'jobs': jobs, 'form': form})
    else:
        form = JobForm()
    return render(request, 'jobs/home_page.html', {'form': form})


def list_job(request):
    jobs = Job.objects.all()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            jobs = Job.objects.filter(name=name)
    else:
        form = JobForm()
    return render(request, 'jobs/list_job.html', {'jobs': jobs, 'form': form})

def apply_job(request):
    if request.method == 'POST':
        form = Apply(request.POST, request.FILES)
        if form.is_valid():
            print('yay')
            return redirect('home-page')
    else:
        form = Apply()
    return render(request, 'jobs/apply_job.html', {'form':form})

def search_job(request):
    if request.method == 'POST':
        print(request.POST)
    else:
        form = JobForm()
    return render(request, 'jobs/search_job.html', {'form': form})




