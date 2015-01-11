from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def still_alive(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated():
            #TODO add the 'next': request.GET.get('next', '')}
            return HttpResponseRedirect(reverse('index'))
        if request.user.character_set.filter(alive=True).exists():
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('create_character'))
    return wrap
