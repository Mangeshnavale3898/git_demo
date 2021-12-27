from django import forms
from .models import Info

class InfoForm(forms.ModelForm):

    name=forms.CharField(
    widget=forms.TextInput(attrs={
        'placeholder':'Enter ur name',
        'class':'form-control'
    })
    )

    uid=forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder':'Enter ur uid',
            'class':'form-control'
        }))

    email=forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder':'Enter ur Email',
            'class':'form-control'
        })
    )
    location=forms.CharField(
    widget=forms.TextInput(attrs={
        'placeholder':'Enter ur location',
        'class':'form-control'
    })
    )
    gen=[
        ("M","Male"),
        ("F","Female"),
        ("O","Other"),
    ]
    gender=forms.ChoiceField(choices=gen,
    widget=forms.RadioSelect()
    )
    cou=[
        ("India","India"),
        ("O","Other"),
    ]
    country=forms.ChoiceField(choices=cou,
    widget=forms.Select(attrs={
        'class':'form-control'
    })
    )
    
    class Meta:
        model=Info
        fields='__all__'

class UpForm(forms.Form):
    uid=forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder':'Enter ur uid',
            'class':'form-control'
    }))
    name=forms.CharField(
    widget=forms.TextInput(attrs={
        'placeholder':'Enter ur new name',
        'class':'form=control'
    })
    )
    
    
class DelForm(forms.Form):
    uid=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'palceholder':'Enter uid to delete record'   
            }
        )
    )
    