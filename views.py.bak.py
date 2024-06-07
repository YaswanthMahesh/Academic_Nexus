from django.shortcuts import render
from django.http import *
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classproject.settings')
django.setup()

from onlineapp.models import *


# Create your views here.

def hello_world(request):
    s = "HELLO World"
    return HttpResponse(s)


def html_page(request):
    s = "<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(s)


def database(request):

    val = College.objects.values('name', 'acronym', 'id')
    return render(request, "index.html", {"values": val})


def studentinfo(request, id):
    s = Student.objects.values('name', 'college__name', 'mocktest1__total').filter(college__id=id)
    return render(request, 'index2.html', {'values': s})
