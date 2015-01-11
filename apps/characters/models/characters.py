from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


from apps.universe.models import Planet
from apps.inventory.models import Ship, Weapon
from apps.items.models import ShipTemplate, WeaponTemplate

from datetime import timedelta



class CharacterValues(models.Model):
    """ hold startingnumbers and other balance values for character classes """
    
    starting_money = models.IntegerField()
    
    
    def __unicode__(self):
        return "Character Values"




class Rank(models.Model):
    """ Ranks are used to unlock Regions, higher missions and setting up corporations """
    
    title = models.CharField(max_length=31)
    level = models.IntegerField(unique=True)
    xp_needed = models.IntegerField()
    unlock = models.TextField(blank=True)
    
    #health = models.IntegerField()
    accuracy = models.FloatField()
    damage = models.FloatField()
    critical = models.FloatField()
    


    def __unicode__(self):
        return "Ranks: %s" % self.name
    
    
    #get the amount of xp needed to level to next rank
    def xp_needed_for_next_rank(self):
        #previous rank xp needed
        start_xp = self.xp_needed_previous_rank()
        level_xp = self.xp_needed - start_xp
        return level_xp
    
    
    
    #get xp needed for previous rank (is the startingpoint for xp to next rank)
    def xp_needed_previous_rank(self):
        try:
            return Rank.objects.get(level = self.level-1).xp_needed
        except Rank.DoesNotExist:
            return 0

    
        
    


class Character(models.Model):
    """ Characters cant die, their ships can """
    
    user = models.ForeignKey(User)
    alive = models.BooleanField(default=True)
    xp = models.IntegerField(default=0)
    rank = models.ForeignKey("characters.Rank")
    created = models.DateField(auto_now_add=True)
    
    name = models.CharField(max_length=31, unique=True)
    planet = models.OneToOneField("universe.Planet")
    money = models.IntegerField()
    
    #current_health = models.IntegerField()
    
    missions = models.IntegerField(default=0)
    duels = models.IntegerField(default=0)
    
    
    def __unicode__(self):
        return self.user.username
    
    
    #create a new character
    @staticmethod
    def create_character(user, name):
        values = CharacterValues.objects.get(id=1)
        rank = Rank.objects.get(level=1)
        character = Character.objects.create(
            user = user,
            name=name,
            rank = rank,
            planet = Planet.objects.all().order_by("?")[0],
            money = values.starting_money,
            #current_health = rank.health,
        )
        
        #set tables
        Timers.objects.create(character=character)
        
        #starting equipment
        character.add_starting_ship()
        character.add_starting_weapons()
        
    
    
    #add starting ship
    def add_starting_ship(self):
        template = ShipTemplate.objects.get(ship_type=ShipTemplate.ROOKIE)
        ship = Ship.randomize_ship(self, self.planet, template)
        ship.active=True
        ship.save()
    
    
    def add_starting_weapons(self):
        for template in WeaponTemplate.objects.filter(
                                    size=ShipTemplate.SMALL, tier=ShipTemplate.TIER_1):
            Weapon.randomize_weapon(self, self.planet, template)
            
    
    
    #xp progres bar
    def xp_progress(self):
        need_for_level = float(self.rank.xp_needed_for_next_rank())
        xp_in_level = float(self.xp - self.rank.xp_needed_previous_rank())
        return "%.2f" % (xp_in_level / need_for_level * 100)
    
    
    
    #shortcuts to acces objects
    def get_ships(self):
        return self.ship_set.filter(planet=self.planet).exclude(active=True)
    
    def get_active_ship(self):
        return self.ship_set.get(planet=self.planet, active=True)
    
    
    
    #see if player has enough money
    def has_enough_money(self, amount):
        if self.money - amount >= 0:
            return True
        else:
            return False
    
    #pay money
    def pay_money(self, amount):
        self.money -= amount
        self.save()
    


class Timers(models.Model):
    """ keep track of cooldowns for action performed by players """
    
    character = models.OneToOneField("characters.Character")
    travel = models.DateTimeField(default=timezone.now())
    simple_mission = models.DateTimeField(default=timezone.now())
    hard_mission = models.DateTimeField(default=timezone.now())
    
    

    def __unicode__(self):
        return "Timers of %s" % self.character.name
    
    
    #Check timers
    def check_timer(self, field):
        if timezone.now() > getattr(self, field):
            return True
        else:
            return False
    
    






