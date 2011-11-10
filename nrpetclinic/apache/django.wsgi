import os.path
import sys

project_home = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", ".."))
app_home = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))\

newrelic_ini_file = os.path.join(os.path.realpath(project_home, "newrelic.ini"))

import newrelic.agent
newrelic.agent.initialize(newrelic_ini_file)

sys.path.append(project_home)
sys.path.append(app_home)       # Per the wsgi site instructions
os.environ['DJANGO_SETTINGS_MODULE'] = 'nrpetclinic.settings_production'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()