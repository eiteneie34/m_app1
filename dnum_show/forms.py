from django import forms
from dnum_show.models import DnumShow

class DnumForm(forms.ModelForm):
    class Meta:
        model = DnumShow
        fields = ['dnumInput', 'precInputDef']
        labels = {'dnumInput': 'Dezimalzahl', 'precInputDef': 'Nachkommastellen'}
        
