from apps.characters.models import Rank, CharacterValues



def add_values():
    CharacterValues.objects.create(
        starting_money = 10000,
    )


def ranks():
    ranks = (
        ("Recruit", 1, 6, 0.3, 1000, 1000), 
        ("Cadet", 2, 12, 0.6, 2500, 1200),
        ("Cadet First Class", 3, 18, 0.9, 5300, 1500),
        ("Squadman", 4, 24, 1.2, 10000, 1900),
        ("Senior Squadman", 5, 30, 1.5, 19000, 2400),
        ("Squad Leader", 6, 36, 1.8, 32000, 3000),
        ("Bannerman", 7, 42, 2.1, 52000, 3700),
        ("Legionary", 8, 48, 2.4, 80000, 4500),
        ("Senior Legionary", 9, 54, 2.7, 118000, 5400),
        ("Sworn Sword", 10, 60, 3, 168000, 6400),
        ("Specialist", 11, 66, 3.3, 232000, 7500),
        ("Senior Specialist", 12, 72, 3.6, 310000, 8700),
        ("Tech Specialist", 13, 78, 3.9, 409000, 10000),
        ("Lieutenant", 14, 84, 4.2, 527000, 11400),
        ("Senior Lieutenant", 15, 90, 4.5, 668000, 12900),
        ("Lieutenant Commander", 16, 96, 4.8, 835000, 14500),
        ("Commander", 17, 102, 5.1, 1030000, 16200),
        ("Senior Commander", 18, 108, 5.4, 1255000, 18000),
        ("Knight Commander", 19, 114, 5.7, 1510000, 19900),
        ("Captain", 20, 120, 6, 1810000, 21900),
        ("Senior Captain", 21, 126, 6.3, 2140000, 24000),
        ("Knight Captain", 22, 132, 6.6, 2520000, 26200),
        ("Marshal", 23, 138, 6.9, 2940000, 28500),
        ("High Marshal", 24, 142, 7.2, 3410000, 30900),
        ("Champion", 25, 150, 7.5, 3930000, 33400),
    )
    
    #Tribe Role Ranks
    #Holdfast Lord       Recruiter of a tribe
    #Ghost               The "hammer" of a tribe
    #Warlord             Leader of a tribe

    
    for rank in ranks:
        Rank.objects.create(
            title = rank[0],
            level = rank[1],
            xp_needed = rank[4],
            accuracy = rank[3]*2,
            critical = rank[3]*2,
            damage = rank[3]*4,
            #health = rank[5],
            unlock = "Some possible extra features",
        )


add_values()
ranks()


