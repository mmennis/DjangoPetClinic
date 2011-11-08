from django.template import Context, loader
from django.http import HttpResponse
from petclinic.models import *
from django.shortcuts import render_to_response

def all_owners(request):
    all_owners = Owner.objects.all()
    return render_to_response('petclinic/owners/all_owners.html', {'all_owners_list': all_owners})
    
def owner(request, owner_id):
    owner = Owner.objects.get(pk=owner_id)
    return render_to_response('petclinic/owners/owner.html', {'owner': owner})
    