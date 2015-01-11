from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib import messages

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.characters.decorators import still_alive
from apps.inventory.models import Ship, Weapon, Fitted
from apps.inventory.forms import HangarFilterForm, WeaponFilterForm
from apps.universe.models import Planet

import pickle


@still_alive
def hangar(request):
    character = request.user.character_set.get(alive=True)
    active = character.get_active_ship()
    
    if request.POST:
        filter_form = HangarFilterForm(request.POST)
        if filter_form.is_valid():
            #get filtered queryset
            ships_qs, planet, per_page = filter_form.get_queryset(request.POST, character)
            request.session["ships_qs"] = pickle.dumps(ships_qs.query)
            request.session["ships_per_page"] = per_page
            request.session["ships_planet"] = planet
    else:
        if "ships_qs" not in request.session:
            request.session["ships_qs"] = pickle.dumps(Ship.objects.filter(planet=character.planet, active=False).query)
            request.session["ships_per_page"] = 15
            request.session["ships_planet"] = character.planet.name
        filter_form = HangarFilterForm(initial={"planet": Planet.objects.get(name=request.session["ships_planet"]).pk})
    
    #pagination
    ships_qs = Ship.objects.all()[:1]
    ships_qs.query = pickle.loads(request.session['ships_qs'])
    paginator = Paginator(ships_qs,
                        request.session['ships_per_page'], request=request)
    page = request.GET.get('page', 1)
    try:
        ships = paginator.page(page)
    except PageNotAnInteger:
        ships = paginator.page(1)
    except EmptyPage:
        ships = paginator.page(paginator.num_pages)
    
    return render(request, "inventory/hangar.html", {"ships": ships, "active": active, "character": character,
                                        "planet": request.session['ships_planet'], "filter_form": filter_form})
    


#perform hangar form actions
@still_alive
def hangar_actions(request):
    pass
    


#perform hangar form actions
@still_alive
def fitting_actions(request):
    pass



@still_alive
def activate_ship(request, pk):
    #see if ship is from user and it exists
    ship = get_object_or_404(Ship, pk=pk)
    character = request.user.character_set.get(alive=True)
    if ship.character == character:
        if ship.planet == character.planet:
            ship.active = True
            ship.save()
            messages.add_message(request, messages.SUCCESS, 'You have activated a %s.' % ship.get_ship_type_display())
    else:
        messages.add_message(request, messages.ERROR, 'This ship could not be activated.')
    return HttpResponseRedirect(reverse("hangar"))
    


@still_alive
def fitting(request):
    character = request.user.character_set.get(alive=True)
    ship = character.get_active_ship()
    
    if request.POST:
        filter_form = WeaponFilterForm(request.POST)
        if filter_form.is_valid():
            #get filtered queryset
            weapons_qs, planet, per_page = filter_form.get_queryset(request.POST, character)
            request.session["weapons_qs"] = pickle.dumps(weapons_qs.query)
            request.session["weapons_per_page"] = per_page
            request.session["weapons_planet"] = planet
    else:
        if "weapons_qs" not in request.session:
            request.session["weapons_qs"] = pickle.dumps(Weapon.objects.filter(planet=character.planet, active=False).query)
            request.session["weapons_per_page"] = 15
            request.session["weapons_planet"] = character.planet.name
        filter_form = WeaponFilterForm(initial={"planet": Planet.objects.get(name=request.session["weapons_planet"]).pk})
    
    #pagination
    weapons_qs = Weapon.objects.all()[:1]
    weapons_qs.query = pickle.loads(request.session['weapons_qs'])
    paginator = Paginator(weapons_qs,
                        request.session['weapons_per_page'], request=request)
    page = request.GET.get('page', 1)
    try:
        weapons = paginator.page(page)
    except PageNotAnInteger:
        weapons = paginator.page(1)
    except EmptyPage:
        weapons = paginator.page(paginator.num_pages)
    
    return render(request, "inventory/fitting.html", {"weapons": weapons, "ship": ship, "character": character,
                                        "planet": request.session['weapons_planet'], "filter_form": filter_form})



#activate a weapon
@still_alive
def activate_weapon(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    character = request.user.character_set.get(alive=True)
    if weapon.character == character:
        ship = character.get_active_ship()
        new = Fitted(ship=ship, weapon=weapon)
        new = new.save()
        if new == False:
            messages.add_message(request, messages.ERROR, 'The weapon could not be fitted to your ship.')
        elif new == None:
            messages.add_message(request, messages.ERROR, 'The weapon size does not fit on your ship.')
        else:
            messages.add_message(request, messages.SUCCESS, 'A weapon has been fitted to your ship.')
    return HttpResponseRedirect(reverse("fitting"))
    



#deactivate weapon
@still_alive
def deactivate_weapon(request, pk):
    fitted = get_object_or_404(Fitted, pk=pk)
    character = request.user.character_set.get(alive=True)
    if fitted.ship.character == character:
        fitted.weapon.active = False
        fitted.weapon.save()
        fitted.delete()
        messages.add_message(request, messages.SUCCESS, 'A weapon has been removed from your ship.')
    else:
        messages.add_message(request, messages.ERROR, 'The weapon could not be removed from your ship.')
    return HttpResponseRedirect(reverse("fitting"))



