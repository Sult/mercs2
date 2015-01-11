from django.db import models


class Planet(models.Model):
    """ Regions """
    
    name = models.CharField(max_length=254, unique=True)
    x = models.IntegerField()
    y = models.IntegerField()
    
    docking_fee = models.IntegerField()
    bounties = models.IntegerField()                    #amount of missions available
    expeditions= models.IntegerField()                  #amount of expeditions available
    
    def __unicode__(self):
        return self.name
    
    




#class Environment(models.Model):
    #""" """
    
    #JUNGLE = ""
    #URBAN = ""
    #MOUNTAINS = ""
    
    
    
    #planet = models.ForeignKey("universe.Planet")
    #name = models.CharField(max_length=254, choices=ENVIRONMENTS)
    #description = models.TextField()
    






