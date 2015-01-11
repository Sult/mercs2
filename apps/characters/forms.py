from django import forms
from django.core.exceptions import ValidationError

from apps.characters.models import Character


class CreateCharacterForm(forms.ModelForm):
    """ choose a name for a new character """
    
    class Meta:
        model = Character
        fields = ["name"]
    
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Character.objects.filter(name__iexact=name):
            raise ValidationError("The name '%s' is already in use." % name)
        
        return name
    
    
    def save(self, user):
        name = self.cleaned_data.get('name')
        Character.create_character(user, name)
