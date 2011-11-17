from petclinic.models import *
from django.shortcuts import render_to_response

import pywapi
import random
import feedparser

def weather(request):
    locations = ["94041", "90008", "97202", "94110", "10024", 
                 "02111", "60605", "23454", "32804", "75204", 
                 "98112", ]
    forecasts = []
    for location in random.sample(locations, 4):
        forecasts.append(pywapi.get_weather_from_yahoo(location))
    return render_to_response("petclinic/weather/weather_basic.html", { 'forecasts': forecasts })


def rss_test(request):
    url = "http://rss.cnn.com/rss/cnn_topstories.rss"
    accessed = []
    feed = feedparser.parse(url.encode('utf-8'), modified = accessed, etag = 100)
    feed_entries = []
    for entry in feed['entries']:
        feed_entries.append(entry)
    
    return render_to_response("petclinic/weather/rss_test.html", { 'feed': feed_entries })