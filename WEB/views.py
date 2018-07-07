from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'StudentIndex.html')

def student(request):
    return render(request, 'Student.html')

def studentLeft(request):
    return render(request, 'StudentLeft.html')
def studentTop(request):
    return render(request, 'StudentTop.html')