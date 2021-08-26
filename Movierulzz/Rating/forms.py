from django import forms

from Rating.models import Cinima_Info


class Cinima_InfoForm(forms.Form):
    mname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name','class': "form-control", 'style': 'width: 500px;' 'border: 2px solid green;'}))
    hero = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Hero', 'style': 'width: 500px;''border: 2px solid yellow;'}))
    heroin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Heroin', 'style': 'width: 500px;''border: 2px solid pink;'}))
    director = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Director', 'style': 'width: 400px;''border: 2px solid #80bfff;'}))
    budget = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Budget', 'style': 'width: 500px;''border: 2px solid  #ff4d94;'}))
    desc=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description', 'style': 'width: 500px;''border: 2px solid #ff4dff;'}))
    poster=forms.ImageField()
class Cinima_InfoModelform(forms.ModelForm):
    class Meta:
        model=Cinima_Info
        fields=['Name','Hero','Heroin','Director','Budget','poster','Desc']


