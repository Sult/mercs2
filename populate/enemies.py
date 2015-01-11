from apps.missions.models import *
from apps.items.models import WeaponTemplate, ShipTemplate


def add_enemy_values():
    EnemyValues.objects.create(
        random_money = 0.2,
        random_xp = 0.1,
        rookie_money = 750,
        rookie_xp = 50,
        frigate_money = 1000,
        frigate_xp = 75,
        destroyer_money = 1500,
        destroyer_xp = 100,
        cruiser_money = 2500,
        cruiser_xp = 125,
        battlecruiser_money = 5000,
        battlecruiser_xp = 150,
        battleship_money = 10000,
        battleship_xp = 175,
        carrier_money = 25000,
        carrier_xp = 200,
        dreadnought_money = 30000,
        dreadnought_xp = 225,
        titan_money = 50000,
        titan_xp = 250,
    )




def add_factions():
    factions = (
        #name, primary, secondary
        ("Ivory Note", WeaponTemplate.LASERS, WeaponTemplate.CANNONS),
        ("Royal Anomalies", WeaponTemplate.CANNONS, WeaponTemplate.LAUNCHERS),
        ("Solar Throne", WeaponTemplate.LAUNCHERS, WeaponTemplate.HYBRIDS),
        ("Vidirium Agency", WeaponTemplate.HYBRIDS, WeaponTemplate.LASERS),
        ("Quantum Curse Association", WeaponTemplate.LASERS, WeaponTemplate.HYBRIDS),
        ("Titan Syndicate", WeaponTemplate.CANNONS, WeaponTemplate.LASERS),
        ("Ironfall", WeaponTemplate.LAUNCHERS, WeaponTemplate.CANNONS),
        ("Ravager's Dissonance", WeaponTemplate.HYBRIDS, WeaponTemplate.LAUNCHERS),
        ("Bloop", WeaponTemplate.LASERS, WeaponTemplate.LAUNCHERS),
        ("Doop", WeaponTemplate.CANNONS, WeaponTemplate.HYBRIDS),
        ("Whiparoo", WeaponTemplate.LAUNCHERS, WeaponTemplate.LASERS),
        ("Whathamacallit", WeaponTemplate.HYBRIDS, WeaponTemplate.CANNONS),
    )
    
    for faction in factions:
        Faction.objects.create(
            name=faction[0],
            primary_weapon=faction[1],
            secondary_weapon=faction[2],
        )


        
    
    

add_enemy_values()
add_factions()
