from django.db import models

from apps.items.models.ships import ShipTemplate

import random


class WeaponValues(models.Model):
    """ weapon balance numbers like volumes of weapons """
    
    small_weapon_volume = models.IntegerField()
    medium_weapon_volume = models.IntegerField()
    large_weapon_volume = models.IntegerField()
    huge_weapon_volume = models.IntegerField()
    colossal_weapon_volume = models.IntegerField()
    
    
    
class WeaponTemplate(models.Model):
    """ Weapons are used for damage. Without a weapon, charaters cant do missions.  """
    
    PULSE_LASER = "pulse_laser"
    BEAM_LASER = "beam_laser"
    AUTOCANNON = "auto_cannon"
    ARTILLERY_CANNON = "artillery_cannon"
    RAGE_LAUNCHER = "rage_launcher"
    JAVALIN_LAUNCHER = "javelin_launcher"
    BLASTER = "blaster"
    RAILGUN = "rail_gun"
    WEAPON_TYPES = (
        (PULSE_LASER, "Pulse Laser"),
        (BEAM_LASER, "Beam Laser"),
        (AUTOCANNON, "Auto Cannon"),
        (ARTILLERY_CANNON, "Artillery Cannon"),
        (RAGE_LAUNCHER, "Rage Launcher"),
        (JAVALIN_LAUNCHER, "Javelin Launcher"),
        (BLASTER, "Blaster"),
        (RAILGUN, "Rail Gun"),
    )
    
    LASERS = "Lasers"
    CANNONS = "Cannons"
    LAUNCHERS = "Launcher"
    HYBRIDS = "Hybrids"
    
    #might add more distances later
    SHORT = "short"
    LONG = "long"
    DISTANCES = (
        (SHORT, "Short"),
        (LONG, "Long"),
    )
    
    
    weapon_type = models.CharField(max_length=254, choices=WEAPON_TYPES)
    size = models.CharField(max_length=254, choices=ShipTemplate.SIZES)
    tier = models.CharField(max_length=254, choices=ShipTemplate.TIERS)
    distance = models.CharField(max_length=254, choices=DISTANCES)
    damage_min_min = models.IntegerField()
    damage_min_max = models.IntegerField()
    damage_max_min = models.IntegerField()
    damage_max_max = models.IntegerField()
    accuracy_min = models.FloatField()
    accuracy_max = models.FloatField()
    critical_min = models.FloatField()
    critical_max = models.FloatField()
    crit_multiplier_min = models.FloatField()
    crit_multiplier_max = models.FloatField()
    
    #magizine
    clip_min = models.IntegerField()
    clip_max = models.IntegerField()
    reload_min = models.IntegerField()
    reload_max = models.IntegerField()
    
    class Meta:
        unique_together = ["weapon_type", "size", "tier"]
    
    def __unicode__(self):
        return self.get_weapon_type_display()

    #random a weapon_typ
    @staticmethod
    def random_weapon_type(**kwargs):
        temp_list = [WeaponTemplate.LASERS, WeaponTemplate.LAUNCHERS, WeaponTemplate.CANNONS, WeaponTemplate.HYBRIDS]
        if "exclude" in kwargs:
            temp_list.remove(kwargs["exclude"])
        return random.choice(temp_list)










