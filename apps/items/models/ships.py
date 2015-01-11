from django.db import models

import random


class ShipTemplate(models.Model):
    """ ships are used to travel from planet to planet, and have their own travel cooldowns and cargobays """
    
    ROOKIE = "rookie"
    FRIGATE = "frigate"
    DESTROYER = "destroyer"
    CRUISER = "cruiser"
    BATTLECRUISER = "battlecruiser"
    BATTLESHIP = "battleship"
    CARRIER = "carrier"
    DREADNOUGHT = "dreadnought"
    TITAN = "titan"
    FREIGHTER = "freighter"
    JUMP_FREIGHTER = "jump-freighter"
    INDUSTRIAL = "industrial"
    BLOCKADE_RUNNER = "blockade_runner"
    SHIP_TYPES = (
        (ROOKIE, "Rookie"),
        (FRIGATE, "Frigate"),
        (DESTROYER, "Destroyer"),
        (CRUISER, "Cruiser"),
        (BATTLECRUISER, "Battlecruiser"),
        (BATTLESHIP, "Battleship"),
        (CARRIER, "Carrier"),
        (DREADNOUGHT, "Dreadnought"),
        (TITAN, "Titan"),
        (FREIGHTER, "Freighter"),
        (JUMP_FREIGHTER, "Jump Freighter"),
        (INDUSTRIAL, "Industrial"),
        (BLOCKADE_RUNNER, "Blockade Runner"),
    )
        
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    HUGE = "huge"
    COLOSSAL = "colossal"
    SIZES = (
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
        (HUGE, "Huge"),
        (COLOSSAL, "Colossal"),
    )
    
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3
    TIERS = (
        (TIER_1, "Tier 1"),
        (TIER_2, "Tier 2"),
        (TIER_3, "Tier 3"),
    )
    
    ship_type = models.CharField(max_length=254, choices=SHIP_TYPES)
    size = models.CharField(max_length=254, choices=SIZES)
    tier = models.IntegerField(choices=TIERS)
    
    hitpoints_min = models.IntegerField()
    hitpoints_max = models.IntegerField()
    armor_min = models.IntegerField()
    armor_max = models.IntegerField()
    weapons_min = models.IntegerField()
    weapons_max = models.IntegerField()
    
    #travel stats
    warp_min = models.DecimalField(max_digits=10, decimal_places=2)
    warp_max = models.DecimalField(max_digits=10, decimal_places=2)
    enter_warp_min = models.IntegerField()
    enter_warp_max = models.IntegerField()
    travel_modifier_min = models.FloatField()
    travel_modifier_max = models.FloatField()
    dock_min = models.IntegerField()
    dock_max = models.IntegerField()
    cargo_space_min = models.IntegerField()
    cargo_space_max = models.IntegerField()
    smuggle_bay_min = models.DecimalField(max_digits=10, decimal_places=1)
    smuggle_bay_max = models.DecimalField(max_digits=10, decimal_places=1)
    
    class Meta:
        unique_together = ["ship_type", "tier"]
    
    def __unicode__(self):
        return self.get_ship_type_display()
        
    
    #randomize max weapons
    #Not really nice but cant think of a shorter way
    @staticmethod
    def random_max_weapons(weapons_min, weapons_max):
        difference = weapons_max - weapons_min
        if difference == 0:
            return weapons_min
        elif difference == 1:
            return random.choice([weapons_min] * 5 + [weapons_max])
        elif difference == 2:
            return random.choice([weapons_min] * 10 + [weapons_min +1] * 3 + [weapons_max])
        else:
            print "Difference bigger than 2 Fuck you messed up"
            return weapons_min
    
