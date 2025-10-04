from django import forms

from .models import (
    Team,
    Player
)

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']


class ProfileFillForm(forms.ModelForm):
    phone = forms.CharField(max_length=13, min_length=10)

    class Meta:
        model = Player
        fields = ['name', 'phone', 'gender', 'college']

class SubmissionConsoleForm(forms.Form):
    team_code = forms.CharField(max_length=128, label="Team Code")
    device_ts = forms.CharField(required=False, widget=forms.HiddenInput())