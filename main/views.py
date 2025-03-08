#from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from . import models
from .forms import formform

def main(request):
    allprojects=models.Projects.objects.all()
    form = formform()
    return render(request, 'main.html', {'projects':allprojects, 'form':form})