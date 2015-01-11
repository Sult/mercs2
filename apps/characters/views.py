from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from apps.characters.decorators import still_alive
from apps.characters.forms import CreateCharacterForm


@login_required
def create_character(request):
    #make sure user does nto have a character that is alive already
    if request.user.character_set.filter(alive=True):
        return HttpResponseRedirect(reverse("index"))
    
    form = CreateCharacterForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save(request.user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "characters/create_character.html", {"form": form})


@login_required
@still_alive
def character(request):
    character = request.user.character_set.get(alive=True)
    
    
    return render(request, "characters/character.html", {"character": character})







