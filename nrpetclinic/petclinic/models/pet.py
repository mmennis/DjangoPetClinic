from django.db import models
from owner import Owner
from pet_type import PetType

class Pet(models.Model):
    name = models.CharField(max_length = 128)
    birth_date = models.DateTimeField("Date of Birth")
    owner = models.ForeignKey(Owner)
    pet_type = models.ForeignKey(PetType)
    
    def __unicode__(self):
        return self.name + "is a " + self.pet_type.name + " and belongs to " + self.owner.first_name + " " + self.owner.last_name
    
    class Meta:
        app_label = 'petclinic'