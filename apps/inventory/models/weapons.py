from django.db import models

from apps.items.models import WeaponTemplate, ShipTemplate

import random

class Weapon(models.Model):
    """ player weapons """
    
    character = models.ForeignKey("characters.Character")
    planet = models.ForeignKey("universe.Planet")
    active = models.BooleanField(default=False)
    template = models.ForeignKey("items.WeaponTemplate")
    damage_min = models.IntegerField()
    damage_max = models.IntegerField()
    accuracy = models.FloatField()
    critical = models.FloatField()
    crit_multiplier = models.FloatField()
    #magizine
    clip = models.IntegerField()
    reload_rounds = models.IntegerField()
    
    def __unicode__(self):
        return "%s %s %s" % (self.character.name, self.template.weapon_type, self.template.size)

    
    
    #generate a random weapon
    @staticmethod
    def randomize_weapon(character, planet, template):
        Weapon.objects.create(
            character = character,
            planet = planet,
            
            template = template,
            damage_min = random.randint(template.damage_min_min, template.damage_min_max),
            damage_max = random.randint(template.damage_max_min, template.damage_max_max),
            accuracy = random.uniform(template.accuracy_min, template.accuracy_max),
            critical = random.uniform(template.critical_min, template.critical_max),
            crit_multiplier = random.uniform(template.crit_multiplier_min, template.crit_multiplier_max),
            #magizine
            clip = random.randint(template.clip_min, template.clip_max),
            reload_rounds = random.randint(template.reload_min, template.reload_max),
        )
    
    
    def show_accuracy(self):
        return int(self.accuracy * 100)
    
    def show_critical(self):
        return int(self.critical * 100)




#Todo make a many to many relation ?
class Fitted(models.Model):
    """ weapons that are fitted to a ship """
    
    ship = models.ForeignKey("inventory.Ship")
    weapon = models.ForeignKey("inventory.Weapon")
    
    def __unicode__(self):
        return "%s: %s" % (self.ship.ship_type, self.weapon.template.weapon_type)
    
    def save(self, *args, **kwargs):
        count = self.ship.fitted_set.all().count()
        if count < self.ship.weapons:
            if self.ship.template.size != self.weapon.template.size:
                return None
            else:
                super(Fitted, self).save(*args, **kwargs)
                self.weapon.active = True
                self.weapon.save()
                return True
        return False
            
    
    
        
        
        
    
