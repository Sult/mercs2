from django.contrib.auth.models import User
from apps.characters.models import Character
from apps.inventory.models import Ship
from apps.items.models import ShipTemplate


#add user
user = User.objects.create_user("admin", "123@234.com", "admin")
user.is_superuser = True
user.save()

execfile("populate/characters.py")
#add items
execfile("populate/weapons.py")
execfile("populate/ships.py")
#addlocations
execfile("populate/planets.py")

execfile("populate/enemies.py")
execfile("populate/missions.py")






Character.create_character(user, "Sult")
char = Character.objects.get(id=1)

#flood some ships for testing
counter = 0
template = ShipTemplate.objects.get(ship_type=ShipTemplate.FRIGATE, tier=ShipTemplate.TIER_1)
while counter < 50:
    Ship.randomize_ship(char, char.planet, template)
    counter+=1
