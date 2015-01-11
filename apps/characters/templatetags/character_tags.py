from django import template

from apps.characters.models import Character

register = template.Library()

@register.filter
def is_alive(user):
    if user.character_set.filter(alive=True):
        return True
    else:
        return False


@register.filter
def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    temp = ""
    
    if days > 0:
        temp += "%dd " % days
    if hours > 0:
        temp += "%dh " % hours
    if mins > 0:
        temp += "%dm " % mins
    if secs > 0:
        temp += "%ds " % secs
    
    return temp


@register.filter
def check_timer(timers, field):
    return timers.check_timer(field)
