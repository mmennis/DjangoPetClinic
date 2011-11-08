from django.template import Context, loader
from django.http import HttpResponse
from petclinic.models import *
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('petclinic/home.html', {})