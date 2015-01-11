from django.db import models
from django.utils import timezone

from apps.missions.models.enemies import Enemy

from datetime import datetime, timedelta

class MissionValues(models.Model):
    """ balance values for missions """
    
    bounty_refresh_min = models.IntegerField()                     #refresh to new mission in seconds
    bounty_refresh_max = models.IntegerField()                     
    




class Bounty(models.Model):
    """ Most basic single player missions Randomizing will be based on fitted ship of character """
    
    character = models.ForeignKey("characters.Character")
    planet = models.ForeignKey("universe.Planet")
    
    class Meta:
        unique_together = ["character", "planet"]
    
    def __unicode__(self):
        return "Mission"
    
    
    #see if some bounties need to be refreshed
    def refresh_enemies(self, character):
        now = timezone.now()
        for enemy in self.enemies.all():
            if enemy.refresh_at < now:
                enemy.delete()
                Bounty.create_enemy(self, character)
    
        


class BountyEnemy(models.Model):
    """ enemies belonging to a bounty """
    
    bounty = models.ForeignKey("missions.Bounty", related_name="enemies")
    enemy = models.ForeignKey("missions.Enemy")
    refresh_at = models.DateTimeField(default=timezone.now())
    price = models.IntegerField()
    
    def __unicode__(self):
        return "bounty enemy"
    
    
    #create a new bounty
    @staticmethod
    def create_enemy(bounty, character):
        values = MissionValues.objects.get(id=1)
        refresh_at = timezone.now() + timedelta(random.randint(values.bounty_refresh_min, values.bounty_refresh_max))
        BountyEnemy.objects.create(
            bounty=bounty,
            enemy=Enemy.random_enemy(character),
            refresh_at=refresh_at,
        )
        
    
    
    
    
    
    
    
    
    
    
    
    
