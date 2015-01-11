from django import forms
from django.core.exceptions import FieldError

from apps.universe.models import Planet
from apps.items.models import ShipTemplate, WeaponTemplate
from apps.inventory.models import Ship, Weapon

from collections import OrderedDict



class HangarFilterForm(forms.Form):
    
    FIELDS = [
        ("", ""),
        ("-weapons", "Weapons"),
        ("good_vs", "Good vs"),
        ("bad_vs", "Bad vs"),
        ("-hitpoints_max", "Hitpoints"),
        ("-armor", "Armor"),
        ("-warp", "Warp"),
        ("-cargo_space", "Cargo Space"),
        ("-smuggle_bay", "Smuggle Bay"),
    ]
    
    PER_PAGE = [
        ("", ""),
        (5, "5 ships"),
        (10, "10 ships"),
        (25, "25 ships"),
        (50, "50 ships"),
    ]
    
    ordered_field_names = ['planet', 'type', 'tier', 'field_1', 'field_2', 'per_page']
    
    field_1 = forms.ChoiceField(choices=FIELDS, label="Stat", required=False)
    #field_2 = forms.ChoiceField(choices=FIELDS, label="Secondary", required=False)
    per_page = forms.ChoiceField(choices=PER_PAGE, required=False)
    
    
    def __init__(self, *args, **kwargs):
        super(HangarFilterForm, self).__init__(*args, **kwargs)
        self.fields['planet'] = forms.ChoiceField(
                            choices=[("all", "All Planets")] + 
                                [ (o.id, o.name) for o in Planet.objects.all().order_by("name")], 
                            required=False)
        self.fields['type'] = forms.ChoiceField(
                            choices=[("", "")] + [ (o[0], o[1]) for o in ShipTemplate.SHIP_TYPES], required=False)
        self.fields['tier'] = forms.ChoiceField(
                            choices=[("", "")] + [ (o[0], o[1]) for o in ShipTemplate.TIERS], required=False)
        
        self.rearrange_field_order()


    def rearrange_field_order(self):

        original_fields = self.fields
        new_fields = OrderedDict()

        for field_name in self.ordered_field_names:
            field = original_fields.get(field_name)
            if field:
                new_fields[field_name] = field

        self.fields = new_fields
    

    
    
    
    #convert postdata to queryset
    def get_queryset(self, postdata, character):
        #get starter queryset based on planet
        planet = self.cleaned_data["planet"]
        if planet:
            try:
                planet = Planet.objects.get(pk=int(planet))
                qs = Ship.objects.filter(character=character, planet=planet, active=False)
                planet = planet.name
            except ValueError, Planet.DoesNotExist:
                planet = "Every Planet"
                qs = Ship.objects.filter(character=character, active=False)
        else:
            qs = Ship.objects.filter(character=character)
            
        
        #filter on ship_type
        ship_type = self.cleaned_data["type"]
        gs = qs.filter(template__ship_type=ship_type)
        
        #order queryset
        temp_list = []
        for temp in [self.cleaned_data['field_1']]:
            if temp:
                temp_list.append(temp)
        
        try:
            qs = qs.order_by(*temp_list)
        except FieldError:
            pass
            
        #get per page
        per_page = self.cleaned_data["per_page"]
        if per_page:
            try:
                per_page = int(per_page)
            except ValueError:
                per_page = 15
        else:
            per_page = 15
        
        return qs, planet, per_page
        
        
        
        
class WeaponFilterForm(forms.Form):
    """ filter weapons """   
    
    PER_PAGE = [
        ("", ""),
        (5, "5 ships"),
        (10, "10 ships"),
        (25, "25 ships"),
        (50, "50 ships"),
    ]
    
    FIELDS = [
        ("", ""),
        ("-damage_min", "Minimal Damage"),
        ("-damage_max", "Maximal Damage"),
        ("template__distance", "Range"),
        ("-accuracy", "Accuracy"),
        ("-critical", "Critical"),
        ("-clip", "Clip"),
        ("template__size", "Size"),
    ]
    
    
    
    field_1 = forms.ChoiceField(choices=FIELDS, label="Stat", required=False)
    #field_2 = forms.ChoiceField(choices=FIELDS, label="Secondary", required=False)
    per_page = forms.ChoiceField(choices=PER_PAGE, required=False)
    
    ordered_field_names = ['planet', 'type', 'tier', 'field_1', 'field_2', 'per_page']
    
    def __init__(self, *args, **kwargs):
        super(WeaponFilterForm, self).__init__(*args, **kwargs)
        self.fields['planet'] = forms.ChoiceField(
                            choices=[("all", "All Planets")] + 
                                [ (o.id, o.name) for o in Planet.objects.all().order_by("name")],
                            required=False)
        self.fields['type'] = forms.ChoiceField(
                            choices=[("", "")] + [ (o[0], o[1]) for o in WeaponTemplate.WEAPON_TYPES], required=False)
        self.fields['tier'] = forms.ChoiceField(
                            choices=[("", "")] + [ (o[0], o[1]) for o in ShipTemplate.TIERS], required=False)
        self.rearrange_field_order()
            
    
    def rearrange_field_order(self):

        original_fields = self.fields
        new_fields = OrderedDict()

        for field_name in self.ordered_field_names:
            field = original_fields.get(field_name)
            if field:
                new_fields[field_name] = field

        self.fields = new_fields
        
        
            #convert postdata to queryset
    def get_queryset(self, postdata, character):
        #get starter queryset based on planet
        planet = self.cleaned_data["planet"]
        if planet:
            try:
                planet = Planet.objects.get(pk=int(planet))
                qs = Weapon.objects.filter(character=character, planet=planet, active=False)
                planet = planet.name
            except ValueError, Planet.DoesNotExist:
                planet = "Every Planet"
                qs = Weapon.objects.filter(character=character, active=False)
        else:
            qs = Weapon.objects.filter(character=character, active=False)
            
        
        #filter on ship_type
        weapon_type = self.cleaned_data["type"]
        qs = qs.filter(template__weapon_type=weapon_type)
        
        #order queryset
        temp_list = []
        for temp in [self.cleaned_data['field_1']]:
            if temp:
                temp_list.append(temp)
        
        try:
            qs = qs.order_by(*temp_list)
        except FieldError:
            pass
            
        #get per page
        per_page = self.cleaned_data["per_page"]
        if per_page:
            try:
                per_page = int(per_page)
            except ValueError:
                per_page = 15
        else:
            per_page = 15
        
        return qs, planet, per_page
        
        
        
        
        
        
        
