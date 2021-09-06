from django.shortcuts import render, redirect
from .models import Post 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def patient_list(request):
    templats = Post.objects.all().order_by('date')
    return render(request, 'patients/patient_list.html', {'kate':templats})

def patient_detail(request, slug):
    # return HttpResponse(slug)
    patient = Post.objects.get(slug=slug)
    return render(request, 'patients/patient_detail.html', {'blath':patient})

@login_required(login_url="/accounts/login/")
def patient_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            database = form.save(commit=False)
            database.author = request.user
            database.save()
            return redirect('patients:list')
    else:    
        form = forms.CreatePost()
    return render(request, 'patients/patient_create.html', {'form':form})