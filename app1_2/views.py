from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Projet2(request):
    return render(request,'app1_2/acceuil.html')
