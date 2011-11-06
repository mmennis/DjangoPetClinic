#!/usr/bin/env python

import sys, os
currPath = os.path.realpath(os.path.dirname(__file__))
sys.path.append(currPath)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

dbDataPath = os.path.join(currPath, 'petclinic', 'db_data')

from django.core.management import setup_environ
from faker import Faker
import datetime
import settings
import random
random.seed

from petclinic.models import *

setup_environ(settings)

f = Faker()

petTypesFile = open(os.path.join(dbDataPath, "pet_types.txt"))
for line in petTypesFile.readlines():
    pt = PetType(name=line.lstrip().rstrip())
    #pt.save()
petTypesFile.close()

specialtiesFile = open(os.path.join(dbDataPath, "specialties.txt"))
for line in specialtiesFile.readlines():
    s = Specialty(name=line.lstrip().rstrip())
    #s.save()
specialtiesFile.close()

petNames = []
petNamesFile = open(os.path.join(dbDataPath, "pet_names.txt"))
for line in petNamesFile.readlines():
    petNames.append(line.lstrip().rstrip())
petNamesFile.close()

petTypes = PetType.objects.all()
specialties = Specialty.objects.all()

for i in range(0,20):
    print random.choice(petTypes)
