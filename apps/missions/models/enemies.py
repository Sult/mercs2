from django.db import models

from apps.items.models import WeaponTemplate, ShipTemplate

import random


class EnemyValues(models.Model):
    """ balance enemy numbers """
    
    random_money = models.FloatField()
    random_xp = models.FloatField()
    rookie_money = models.IntegerField()
    rookie_xp = models.IntegerField()
    frigate_money = models.IntegerField()
    frigate_xp = models.IntegerField()
    destroyer_money = models.IntegerField()
    destroyer_xp = models.IntegerField()
    cruiser_money = models.IntegerField()
    cruiser_xp = models.IntegerField()
    battlecruiser_money = models.IntegerField()
    battlecruiser_xp = models.IntegerField()
    battleship_money = models.IntegerField()
    battleship_xp = models.IntegerField()
    carrier_money = models.IntegerField()
    carrier_xp = models.IntegerField()
    dreadnought_money = models.IntegerField()
    dreadnought_xp = models.IntegerField()
    titan_money = models.IntegerField()
    titan_xp = models.IntegerField()
    
    
    
    def __unicode__(self):
        return "Enemy Values"
        


class Faction(models.Model):
    """ Different enemies have their own choice of weapons """
    
    
    name = models.CharField(max_length=254, unique=True)
    primary_weapon = models.CharField(max_length=254, choices=WeaponTemplate.WEAPON_TYPES)
    secondary_weapon = models.CharField(max_length=254, choices=WeaponTemplate.WEAPON_TYPES)
    
    def __unicode__(self):
        return self.name
        
    
    #get a random faction
    @staticmethod
    def random_faction():
        return Faction.objects.all().order_by("?")[0]
    
    


class Enemy(models.Model):
    """ actual enemies to fight """
    
    EASY = 4
    NORMAL = 3
    HARD = 2
    EXTREME = 1
    DIFFICULTIES = (
        (EASY, "Easy"),
        (NORMAL, "Normal"),
        (HARD, "Hard"),
        (EXTREME, "Extreme"),
    )
    
    faction = models.ForeignKey("missions.Faction")
    template = models.ForeignKey("items.ShipTemplate")
    
    difficulty = models.IntegerField(choices=DIFFICULTIES)
    hitpoints = models.IntegerField()
    armor = models.IntegerField()
    weapons = models.IntegerField()

    def __unicode__(self):
        return "Enemy: %s(%s)" % (self.template.get_shipt_type_display(), self.faction.name)
    
    
    #get a random difficulty
    @staticmethod
    def random_difficulty():
        temp = random.choice(Enemy.DIFFICULTIES)
        return temp[0]
        
    
    #random a enemy based on current player ship
    @staticmethod
    def random_enemy(character, **kwargs):
        template = character.get_active_ship().template
        if "faction" in kwargs:
            faction = kwargs['faction']
        else:
            faction = Faction.objects.all().order_by("?")[0]
        
        if "difficulty" in kwargs:
            difficulty = kwargs["difficulty"]
        else:
            difficulty = Enemy.random_difficulty()
        
        enemy = Enemy.objects.create(
            faction = faction,
            template = template,
            difficulty = difficulty,
    
            hitpoints = random.randint((template.hitpoints_min / difficulty), (template.hitpoints_max / difficulty)),
            armor = random.randint((template.armor_min / difficulty), (template.armor_max / difficulty)),
            weapons = ShipTemplate.random_max_weapons(template.weapons_min, template.weapons_max),
        )
        enemy.add_weapons()
        return enemy
    
    
    #add weapons to enemy
    def add_weapons(self):
        counter = 0
        while counter < self.weapons:
            counter += 1
            EnemyWeapon.randomize_weapon(self, self.get_weapon_template)
    
    
    #get enemy weapon template
    def get_weapon_template(self):
        weapon_type = random.choice([self.factuion.primary_weapon]*3 + [self.secondary_weapon])
        return WeaponTemplate.objects.get(weapon_type=weapon_type, size=self.template.size, tier=self.template.tier)
        
        


class EnemyWeapon(models.Model):
    """ player weapons """
    
    enemy = models.ForeignKey("missions.Enemy")
    template = models.ForeignKey("items.WeaponTemplate")
    damage_min = models.IntegerField()
    damage_max = models.IntegerField()
    accuracy = models.FloatField()
    critical = models.FloatField()
    crit_multiplier = models.FloatField()
    #magizine
    clip = models.IntegerField()
    reload_rounds = models.IntegerField()

    def __unicode__(self):
        return "Enemy Weapon"
    
    
    #generate a random weapon
    @staticmethod
    def randomize_weapon(enemy, template):
        Weapon.objects.create(
            enemy = enemy,           
            template = template,
            damage_min = random.randint(template.damage_min_min, template.damage_min_max),
            damage_max = random.randint(template.damage_max_min, template.damage_max_max),
            accuracy = random.uniform(template.accuracy_min, template.accuracy_max),
            critical = random.uniform(template.critical_min, template.critical_max),
            crit_multiplier = random.uniform(template.crit_multiplier_min, template.crit_multiplier_max),
            #magizine
            clip = random.randint(template.clip_min, template.clip_max),
            reload_rounds = random.randint(template.reload_min, template.reload_max),
        )






