from apps.items.models import *
from apps.inventory.models import *



def add_ship_values():
    ShipValues.objects.create(
        travel_time_multiplier = 5.0,
        travel_cost = 20,
    )
    


def add_rookie():
    ShipTemplate.objects.create(
        ship_type = ShipTemplate.ROOKIE,
        size = ShipTemplate.SMALL,
        tier = ShipTemplate.TIER_1,
    
        hitpoints_min = 600,
        hitpoints_max = 600,
        armor_min = 80,
        armor_max = 80,
        weapons_min = 2,
        weapons_max = 2,
    
        #travel stats
        warp_min = 3,
        warp_max = 3,
        enter_warp_min = 20,
        enter_warp_max = 20,
        travel_modifier_min = 1.00,
        travel_modifier_max = 1.00,
        dock_min = 60,
        dock_max = 60,
        cargo_space_min = 10,
        cargo_space_max = 10,
        smuggle_bay_min = 0.30,
        smuggle_bay_max = 0.30,
    )



def add_frigate():
    ShipTemplate.objects.create(
        ship_type = ShipTemplate.FRIGATE,
        size = ShipTemplate.SMALL,
        tier = ShipTemplate.TIER_1,
    
        hitpoints_min = 600,
        hitpoints_max = 900,
        armor_min = 100,
        armor_max = 220,
        weapons_min = 2,
        weapons_max = 3,
    
        #travel stats
        warp_min = 3.00,
        warp_max = 5.00,
        enter_warp_min = 13,
        enter_warp_max = 18,
        travel_modifier_min = 0.80,
        travel_modifier_max = 1.00,
        dock_min = 40,
        dock_max = 60,
        cargo_space_min = 10,
        cargo_space_max = 20,
        smuggle_bay_min = 0.30,
        smuggle_bay_max = 0.50,
    )



def add_frigate_t2():
    ShipTemplate.objects.create(
        ship_type = ShipTemplate.FRIGATE,
        size = ShipTemplate.SMALL,
        tier = ShipTemplate.TIER_2,
    
        hitpoints_min = 800,
        hitpoints_max = 1100,
        armor_min = 180,
        armor_max = 300,
        weapons_min = 2,
        weapons_max = 4,
    
        #travel stats
        warp_min = 4.00,
        warp_max = 6.00,
        enter_warp_min = 10,
        enter_warp_max = 15,
        travel_modifier_min = 0.80,
        travel_modifier_max = 1.10,
        dock_min = 30,
        dock_max = 50,
        cargo_space_min = 15,
        cargo_space_max = 25,
        smuggle_bay_min = 0.45,
        smuggle_bay_max = 0.80,
    )



def add_destroyer_t1():
    ShipTemplate.objects.create(
        ship_type = ShipTemplate.DESTROYER,
        size = ShipTemplate.SMALL,
        tier = ShipTemplate.TIER_1,
    
        hitpoints_min = 700,
        hitpoints_max = 1000,
        armor_min = 200,
        armor_max = 300,
        weapons_min = 3,
        weapons_max = 4,
    
        #travel stats
        warp_min = 3.00,
        warp_max = 5.00,
        enter_warp_min = 15,
        enter_warp_max = 20,
        travel_modifier_min = 1.10,
        travel_modifier_max = 1.40,
        dock_min = 45,
        dock_max = 75,
        cargo_space_min = 15,
        cargo_space_max = 30,
        smuggle_bay_min = 0.30,
        smuggle_bay_max = 0.50,
    )


def add_destroyer_t2():
    ShipTemplate.objects.create(
        ship_type = ShipTemplate.DESTROYER,
        size = ShipTemplate.SMALL,
        tier = ShipTemplate.TIER_2,
    
        hitpoints_min = 900,
        hitpoints_max = 1200,
        armor_min = 250,
        armor_max = 350,
        weapons_min = 3,
        weapons_max = 5,
    
        #travel stats
        warp_min = 3.50,
        warp_max = 5.50,
        enter_warp_min = 13,
        enter_warp_max = 17,
        travel_modifier_min = 1.10,
        travel_modifier_max = 1.40,
        dock_min = 35,
        dock_max = 65,
        cargo_space_min = 20,
        cargo_space_max = 35,
        smuggle_bay_min = 0.45,
        smuggle_bay_max = 0.80,
    )
    
    

add_ship_values()
add_rookie()
add_frigate()
add_frigate_t2()
add_destroyer_t1()
add_destroyer_t2()










