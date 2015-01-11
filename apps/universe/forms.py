from django import forms
from django.utils import timezone
from django.contrib import messages

from apps.universe.models import Planet

from datetime import timedelta



def travel_character(postdata, character):
    try:
        pk = int(postdata['destination'])
        destination = Planet.objects.get(pk=pk)
    except ValueError, Planet.DoesNotExist:
        return "This place does not exist!", messages.ERROR
    
    if not character.timers.check_timer("travel"):
        return "Your ship is still recharging from your last trip.", messages.ERROR
    
    #get travel info
    ship = character.get_active_ship()
    travel_info = ship.travel_information(destination)
    
    if not character.has_enough_money(travel_info.cost):
        return "You do not have enough money to travel to %s." % travel_info.name, messages.ERROR
    
    #all requirements met, update objects
    character.pay_money(travel_info.cost)
    character.planet = destination
    character.save()
    character.timers.travel = timezone.now() + timedelta(seconds=travel_info.duration)
    character.timers.save()
    ship.planet = destination
    ship.save()









