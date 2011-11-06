from django.db import models

class PetType(models.Model):
    name = models.CharField(max_length = 128)
    
    def __unicode__(self):
        return "Pet type: " + self.name
    
    class Meta:
        app_label = 'petclinic'