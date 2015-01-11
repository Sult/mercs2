from apps.items.models import *
from apps.characters.models import Rank


def weapon_values():
    WeaponValues.objects.create(
        small_weapon_volume = 5,
        medium_weapon_volume = 10,
        large_weapon_volume = 50,
        huge_weapon_volume = 400,
        colossal_weapon_volume = 4000,
    )


def add_small_weapons():
    weapons = (
        [WeaponTemplate.PULSE_LASER, WeaponTemplate.SHORT,  [0.8, 8, 0.05, 1.7, 24, 3],
                                                            [0.9, 15, 0.1, 2.2, 32, 4]],
        [WeaponTemplate.BEAM_LASER, WeaponTemplate.LONG,    [0.3, 24, 0.1, 2, 13, 4],
                                                            [0.42, 30, 0.16, 3, 18, 5]],
        [WeaponTemplate.AUTOCANNON, WeaponTemplate.SHORT,   [0.5, 14, 0.07, 1.9, 12, 2],
                                                            [0.62, 21, 0.13, 2.2, 18, 3]],
        [WeaponTemplate.ARTILLERY_CANNON, WeaponTemplate.LONG,  [0.3, 23, 0.2, 2, 7, 3],
                                                                [0.41, 28, 0.28, 2.4, 11, 4]],
        [WeaponTemplate.RAGE_LAUNCHER, WeaponTemplate.SHORT,    [0.75, 11, 0.24, 1.2, 8, 4],
                                                                [0.87, 16, 0.35, 1.4, 11, 6]],
        [WeaponTemplate.JAVALIN_LAUNCHER, WeaponTemplate.LONG,  [0.45, 20, 0.1, 2.2, 4, 2],
                                                                [0.5, 29, 0.18, 2.35, 6, 3]],
        [WeaponTemplate.BLASTER, WeaponTemplate.SHORT,      [0.52, 12, 0.15, 1.6, 21,4],
                                                            [0.63, 19, 0.24, 1.8, 29, 5]],
        [WeaponTemplate.RAILGUN, WeaponTemplate.LONG,       [0.69, 9, 0.12, 1.6, 18, 3],
                                                            [0.81, 15, 0.22, 1.95, 22, 4]],
    )
    
    for weapon in weapons:
        temp = weapon[3][1] - weapon[2][1]
        min_min = weapon[2][1]
        min_max = weapon[2][1] + int(temp/2)
        max_min = weapon[3][1] - int(temp/2)
        max_max = weapon[3][1]
        wep = WeaponTemplate.objects.create(
            weapon_type = weapon[0],
            size = ShipTemplate.SMALL,
            tier=ShipTemplate.TIER_1,
            distance = weapon[1],
            accuracy_min = weapon[2][0],
            accuracy_max = weapon[3][0],
            damage_min_min = min_min,
            damage_min_max = min_max,
            damage_max_min = max_min,
            damage_max_max = max_max,
            critical_min = weapon[2][2],
            critical_max = weapon[3][2],
            crit_multiplier_min = weapon[2][3],
            crit_multiplier_max = weapon[3][3],
            clip_min = int(weapon[2][4] / 2),
            clip_max = int(weapon[3][4] / 2),
            reload_min = int(weapon[2][5] / 2),
            reload_max = int(weapon[3][5] / 2),
        )
    
    

weapon_values()
add_small_weapons()
        
        
        
        
