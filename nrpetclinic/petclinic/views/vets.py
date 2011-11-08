from django.template import Context, loader
from django.http import HttpResponse
from petclinic.models import *
from django.shortcuts import render_to_response

def all_vets(request):
    all_vets = Vet.objects.all()
    return render_to_response('petclinic/vets/all_vets.html', { 'all_vets_list': all_vets })
    
def vet(request, vet_id):
    vet = Vet.objects.get(pk=vet_id)
    return render_to_response('petclinic/vets/vet.html', {'vet': vet})