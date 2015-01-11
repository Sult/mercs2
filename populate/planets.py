from apps.universe.models import *

import random

def add_planets():
    names = (
        "Zaqfag",
        "Corholt",
        "Byrock",
        "Eastwilde",
        "Mallow",
        "Aelville",
        "Larston",
        "Wester",
        "Groton",
        "Ironston",
    )
    
    for name in names:
        Planet.objects.create(
            name=name,
            x=random.randint(1, 450),
            y=random.randint(1, 450),
            docking_fee=random.randint(200, 450),
            bounties=random.randint(5,8),
            expeditions=random.randint(3,5),
        )
        

add_planets()
