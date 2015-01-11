from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from apps.characters.decorators import still_alive
from apps.universe.forms import travel_character


@still_alive
def travel(request):
    character = request.user.character_set.get(alive=True)
    ship = character.get_active_ship()
    
    if "destination" in request.POST:
        travel_character(request.POST, character)
        
    travel_form = ship.travel_form()
    
    return render(request, "world/travel.html", {"character": character, "travel_form": travel_form})
    
