from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from apps.characters.decorators import still_alive

from apps.missions.models import Bounty


@still_alive
def bounty(request):
    character = request.user.character_set.get(alive=True)
    bounty, created = Bounty.objects.get_or_create(character=character, planet=character.planet)
    
    
    
    
