from django.db import models

from pet import Pet

class Visit(models.Model):
    visit_date = models.DateTimeField()
    description = models.TextField()
    pet = models.ForeignKey(Pet)
    
    class Meta:
        app_label = 'petclinic'
        
