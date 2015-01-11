from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth.models import User

from apps.users.forms import LoginForm, RegistrationForm
from apps.characters.models import Character


def index(request):
    login_form = LoginForm(request.POST or None)
    
    if request.POST and login_form.is_valid():
        user = login_form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('next') or reverse('index'))
    
    if request.user.is_authenticated():
        #check if user has a character that is alive
        if not Character.objects.filter(user=request.user, alive=True):
            return HttpResponseRedirect(reverse("create_character"))
    
    return render(request, "users/index.html", {"login_form": login_form, 'next': request.GET.get('next', '')})
    
    
    
    #return render(request, "index.html", {"login_form": login_form})



# Register new user
def register_user(request):
    #make sure user is not already logged in
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("index"))
    
    form = RegistrationForm(request.POST or None)
    login_form = LoginForm()
    # False till someone fills in and sends
    if request.POST and form.is_valid():
        new_user = form.save()
        #create starting templates
        
        #send confiermationmail blabla
        
        return HttpResponseRedirect(reverse('register succes'))
    
    return render(request, 'users/register.html', {'form': form, "login_form": login_form})
    


def register_succes(request):
    login_form = LoginForm(request.POST or None)
    return render(request, "users/register_succes.html", {"login_form": login_form})



@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))



########### Information pages

def contact(request):
    login_form = LoginForm()
            
    return render(request, "users/contact.html", {"login_form": login_form})





