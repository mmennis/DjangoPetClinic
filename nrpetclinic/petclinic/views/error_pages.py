from petclinic.models import *
from django.shortcuts import render_to_response

def exception_page(request):
    raise NameError("This is a test error")
    return render_to_response("petclinic/error_pages/exception_page.html")

def divide_by_zero(request):
    ans = 1/0
    return render_to_response("petclinic/error_pages/divide_by_zero.html", {'ans' : ans})