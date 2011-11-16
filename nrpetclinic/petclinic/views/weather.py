from petclinic.models import *
from django.shortcuts import render_to_response

import pywapi
import random

def weather(request):
    locations = ["94041", "90008", "97202", "94110", "10024", 
                 "02111", "60605", "23454", "32804", "75204", 
                 "98112", ]
    forecasts = []
    for location in random.sample(locations, 4):
        forecasts.append(pywapi.get_weather_from_yahoo(location))
    return render_to_response("petclinic/weather/weather_basic.html", { 'forecasts': forecasts })