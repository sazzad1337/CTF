from django import forms
from players import models

class PlayerRegister(forms.ModelForm):
    class Meta:
        model = models.players_list
        fields = "__all__"