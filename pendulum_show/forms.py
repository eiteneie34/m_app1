
from django import forms
from pendulum_show.models import PenShow

class PenShowForm(forms.ModelForm):
    class Meta:
        model = PenShow
        fields = [
            'alpha_grad',
            'g',
            'l',
            'm',
            'deltaR',
            'anzahlT'
        ]
        gstr = 'Gravitationsbeschleunigung g in m/s^2'
        labels = {
            'alpha_grad': 'Auslenkungswinkel alpha in Grad',
            'g': 'Gravitationsbeschleunigung g in m / s^2',
            'l': 'Länge des Pendels l in m',
            'm':'Masse des Pendelkörpers m',
            'deltaR': 'Dämpfungskonstante der Reibungskraft delta in kg/s',
            'anzahlT': 'Anzahl der Perioden des harmonischen Pendels',
        }
