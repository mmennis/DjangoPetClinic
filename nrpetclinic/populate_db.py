#!/usr/bin/env python

import sys, os
currPath = os.path.realpath(os.path.dirname(__file__))
sys.path.append(currPath)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

dbDataPath = os.path.join(currPath, 'petclinic', 'db_data')

from django.core.management import setup_environ
from faker import Faker
import datetime, settings, random
random.seed

OWNER_COUNT = 100
VET_COUNT = 100

from petclinic.models import *

setup_environ(settings)

f = Faker()

petTypesFile = open(os.path.join(dbDataPath, "pet_types.txt"))
for line in petTypesFile.readlines():
    pt = PetType(name=line.lstrip().rstrip())
    pt.save()
petTypesFile.close()

specialtiesFile = open(os.path.join(dbDataPath, "specialties.txt"))
for line in specialtiesFile.readlines():
    s = Specialty(name=line.lstrip().rstrip())
    s.save()
specialtiesFile.close()

petNames = []
petNamesFile = open(os.path.join(dbDataPath, "pet_names.txt"))
for line in petNamesFile.readlines():
    petNames.append(line.lstrip().rstrip())
petNamesFile.close()

petTypes = PetType.objects.all()
all_specialties = Specialty.objects.all()

for i in range(0,OWNER_COUNT):
    o = Owner(first_name=f.first_name(),
              last_name=f.last_name(),
              address=f.street_address(),
              city=f.city(),
              telephone="1-123-555-1212")
    o.save()
    for j in range(0,random.randint(0,4)):
        p = Pet(name=random.choice(petNames),
                pet_type=random.choice(petTypes),
                birth_date=datetime.datetime.now(),
                owner=o)
        p.save()
        for k in range(0, random.randint(0,4)):
            v = Visit(visit_date=datetime.datetime.now(),
                      description=f.lorem(),
                      pet=p)
            v.save()


for l in range(0, VET_COUNT):
    vet = Vet(first_name=f.first_name(), last_name=f.last_name())
    vet.save()
    for m in range(0, random.randint(0, 4)):
        vet.specialties.add(random.choice(all_specialties))
    vet.save()