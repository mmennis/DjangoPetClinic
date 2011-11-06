from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length = 128)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        app_label = 'petclinic'