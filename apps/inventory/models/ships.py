from django.db import models

from apps.universe.models import Planet
from apps.items.models import ShipTemplate, WeaponTemplate
from apps.utils import random_decimal

import random, math
from collections import namedtuple


class ShipValues(models.Model):
    """ ship balance numbers """
    
    travel_time_multiplier = models.FloatField()
    travel_cost = models.IntegerField()
    
    


class Ship(models.Model):
    """ ships a character has gained """
    
    character = models.ForeignKey("characters.Character")
    planet = models.ForeignKey("universe.Planet")
    active = models.BooleanField(default=False)
    
    #ship_type = models.CharField(max_length=244, choices=ShipTemplate.SHIP_TYPES)
    #tier = models.IntegerField(choices=ShipTemplate.TIERS)
    template = models.ForeignKey("items.ShipTemplate")
    hitpoints_current = models.IntegerField()
    hitpoints_max = models.IntegerField()
    armor = models.IntegerField()
    weapons = models.IntegerField()
    good_vs = models.CharField(max_length=254, choices=WeaponTemplate.WEAPON_TYPES)
    bad_vs = models.CharField(max_length=254, choices=WeaponTemplate.WEAPON_TYPES)
    
    warp = models.DecimalField(max_digits=10, decimal_places=2)
    enter_warp = models.IntegerField()
    travel_modifier = models.FloatField()
    dock = models.IntegerField()
    cargo_space = models.IntegerField()
    smuggle_bay = models.DecimalField(max_digits=10, decimal_places=1)
    
    
    def __unicode__(self):
        return "%s, %s: %s" % (self.character.name, self.planet.name, self.get_ship_type_display())
    
    
    #make sure every character can only have one active ship
    def save(self, *args, **kwargs):
        if self.active:
            try:
                ship = Ship.objects.get(character=self.character, active=True)
                ship.active=False
                ship.save()
            except Ship.DoesNotExist:
                pass
        super(Ship, self).save(*args, **kwargs)
    
    
    #randomize and add ship
    @staticmethod
    def randomize_ship(character, planet, template):
        hitpoints = random.randint(template.hitpoints_min, template.hitpoints_max)
        good_vs = WeaponTemplate.random_weapon_type()
        bad_vs = WeaponTemplate.random_weapon_type(exclude=good_vs)
        
        ship = Ship.objects.create(
            character = character,
            planet = planet, 
            template = template,
            hitpoints_current = hitpoints,
            hitpoints_max = hitpoints,
            armor = random.randint(template.armor_min, template.armor_max),
            weapons = ShipTemplate.random_max_weapons(template.weapons_min, template.weapons_max),
            good_vs = good_vs,
            bad_vs = bad_vs,
            warp = random_decimal(template.warp_min, template.warp_max),
            enter_warp = random.randint(template.enter_warp_min, template.enter_warp_max),
            travel_modifier = random.uniform(template.travel_modifier_min, template.travel_modifier_max),
            dock = random.randint(template.dock_min, template.dock_max),
            cargo_space = random.randint(template.cargo_space_min, template.cargo_space_max),
            smuggle_bay = random_decimal(template.smuggle_bay_min, template.smuggle_bay_max),
        )
        return ship
    

    
    #create a list of possible destinations with their base price and base traveltime
    def travel_form(self):
        destinations = Planet.objects.exclude(pk=self.planet.pk).order_by("name")
        dest_list = []
        for destination in destinations:
            dest_list.append(self.travel_information(destination))
        return dest_list
    
    
    
    #get the distance between 2 planets
    @staticmethod
    def get_distance(home, destination):
        delta_x = float(destination.x - home.x)
        delta_y = float(destination.y - home.y)
        
        csquare = (delta_x ** 2) + (delta_y ** 2)
        return math.sqrt(csquare)


    #warptime
    def warp_time(self, distance):
        return distance / float(self.warp)
    
    #get travelduration
    def travel_duration(self, distance, values):
        engage_warp = 2 * self.enter_warp                                     # enter warp and get out of warp
        docking = 2* self.dock
        duration = int(docking + engage_warp + self.warp_time(distance) * values.travel_time_multiplier)
        return duration
    
    
    #in fuel
    def get_travel_cost(self, distance, destination, values):
        return int(distance * self.travel_modifier * values.travel_cost + destination.docking_fee)
        
        
        
    
    def travel_information(self, destination):
        values = ShipValues.objects.get(id=1)
        TravelCost = namedtuple("TravelCost", "pk name duration cost")
        distance = self.get_distance(self.planet, destination)
        return TravelCost(name=destination.name, pk=destination.pk,
                duration=self.travel_duration(distance, values), 
                cost=self.get_travel_cost(distance, destination, values))
        
        




    
