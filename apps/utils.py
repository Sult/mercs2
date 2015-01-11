import random



#ranomize a decimal value (to 2 decimalplaces maximal)
def random_decimal(low, high):
    low *= 100
    high *= 100
    return float(random.randint(low, high)) / 100



