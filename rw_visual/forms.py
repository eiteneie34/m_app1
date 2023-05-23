from django import forms
from rw_visual.models import RwVisual

class RwVisualForm(forms.ModelForm):
    class Meta:
        model = RwVisual
        fields = [
            'num_points',
            'x_distance',
            'y_distance',
            'dot_marker',
            'dot_size',
            'dot_alpha',
            'dot_size_v',
            'dot_alpha_v',
            'dot_color',
            'dot_cmap',
            'ax_color',

        ]
        labels = {
            'num_points': 'Anzahl der Schritte',
            'x_distance': 'Horizontale Abweichung',
            'y_distance': 'Senkrechte Abweichung',
            'dot_marker': 'Form des Punktes',
            'dot_size': 'Punktgröße',
            'dot_alpha': 'Transparenz der Punkte - bei 1 - intransparent',
            'dot_size_v': 'Zufällige Veränderung der Punktgröße bis zu 500 %',
            'dot_alpha_v': 'Zufällige Veränderung der Transparenz der Punkte bis zu 20 %',
            'dot_color': 'Punktfarbe',
            'dot_cmap': 'Farbverlauf der Punkte',
            'ax_color': 'Hintergrundfarbe',
        }




