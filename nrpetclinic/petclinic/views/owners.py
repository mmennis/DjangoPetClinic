from petclinic.models import *
from django.shortcuts import render_to_response

def all_owners(request):
    if 'last_name' in request.GET:
        all_owners = Owner.objects.filter(last_name__icontains=request.GET['last_name'])
    else:
        all_owners = Owner.objects.all()
    return render_to_response('petclinic/owners/all_owners.html', {'all_owners_list': all_owners})
    
def owner(request, owner_id):
    owner = Owner.objects.get(pk=owner_id)
    return render_to_response('petclinic/owners/owner.html', {'owner': owner})

def find_owners(request):
    return render_to_response("petclinic/owners/find_owners.html", {})
    