from django.db import models
from m_app1s.models import Entry


class RwVisual(models.Model):
    """random pattern app model"""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    num_points_choices = (
        ('10', '10'),
        ('25', '25'), ('50', '50'), ('75', '75'), ('100', '100'),
        ('250', '250'), ('500', '500'), ('750', '750'), ('1000', '1000'),
        ('2500', '2500'), ('5000', '5000'), ('7500', '7500'), ('10000', '10000'),
        ('15000', '15000'), ('20000', '20000'), ('25000', '25000'), ('30000', '30000'),
    )
    num_points = models.CharField(default='1000', max_length=50, choices=num_points_choices)

    x_distance_choices = (
        ('0 1 2 3 4 5', '0 1 2 3 4 5'),
        ('0 1 1 1 3 4', '0 1 1 1 3 4'),
        ('0 1 3 4 4 4', '0 1 3 4 4 4'),
    )
    x_distance = models.CharField(default='0 1 2 3 4', max_length=50, choices=x_distance_choices)

    y_distance_choices = (
        ('0 1 2 3 4 5', '0 1 2 3 4 5'),
        ('0 1 1 1 3 4', '0 1 1 1 3 4'),
        ('0 1 3 4 4 4', '0 1 3 4 4 4'),
    )
    y_distance = models.CharField(default='0 1 2 3 4', max_length=50, choices=y_distance_choices)

    x_values = models.CharField(default='0 1 2 3 4', max_length=1000000)
    y_values = models.CharField(default='0 1 2 3 4', max_length=1000000)
    point_numbers_random = models.CharField(default='0 1 2 3 4', max_length=1000000)
    dot_size_v = models.BooleanField(default=False)
    dot_alpha_v = models.BooleanField(default=False)
    dot_marker_choices = (
        ('.', 'Punkt'),
        ('o', 'Kreis'),
        ('s', 'Quadrat'),
        ('^', 'Dreieck ^'),
        ('v', 'Dreieck v'),
        ('8', 'Octagon'),
        ('D', 'Diamant'),
        ('d', 'Rombe'),
        ('p', 'Pentagon'),
        ('H', 'Hexagon'),
        ('(4,1)', 'Stern 4'),
        ('*', 'Stern 5'),
        ('(7,1)', 'Stern 7'),
        ('(8,1)', 'Stern 8'),
        ('(9,1)', 'Stern 9'),
        ('(5,2)', 'Schneeflocke 5'),
        ('(6,2)', 'Schneeflocke 6'),
        ('(7,2)', 'Schneeflocke 7'),
        ('(8,2)', 'Schneeflocke 8'),
        ('(9,2)', 'Schneeflocke 9'),

    )
    dot_marker = models.CharField(default='.', max_length=10, choices=dot_marker_choices)
    dot_size_choices = (
        ('1', '1'), ('5', '5'), ('10', '10'), ('50', '50'), ('100', '100'), ('250', '250'),
        ('500', '500'), ('750', '750'), ('1000', '1000'), ('2500', '2500'), ('5000', '5000'), ('7500', '7500'),
        ('10000', '10000'),
    )
    dot_size = models.CharField(default='5.0', max_length=10, choices=dot_size_choices)
    dot_alpha_choices = (
        ('0.1', '0,1'), ('0.2', '0,2'), ('0.3', '0,3'), ('0.4', '0.4'), ('0.5', '0.5'),
        ('0.6', '0,6'), ('0.7', '0,7'), ('0.8', '0,8'), ('0.9', '0,9'), ('1.0', '1'),
    )
    dot_alpha = models.CharField(default='1.0', max_length=10, choices=dot_alpha_choices)
    dot_color_choices = (
        ('white', 'white'), ('whitesmoke', 'whitesmoke'), ('lightgray', 'lightgray'), ('gray', 'gray'), ('dimgray', 'dimgray'), ('black', 'black'),
        ('mistyrose', 'mistyrose'), ('lightcoral', 'lightcoral'), ('coral', 'coral'), ('red', 'red'), ('brown', 'brown'), ('maroon', 'maroon'),
        ('beige', 'beige'), ('yellow', 'yellow'), ('gold', 'gold'), ('orange', 'orange'), ('chocolate', 'chocolate'), ('sienna', 'sienna'),
        ('ivory', 'ivory'), ('lightgreen', 'lightgreen'), ('lime', 'lime'),  ('green', 'green'), ('darkgreen', 'darkgreen'), ('olive', 'olive'),
        ('azure', 'azure'), ('aqua', 'aqua'), ('turquoise', 'turquoise'),  ('teal', 'teal'), ('darkslategray', 'darkslategray'),
        ('lightblue', 'lightblue'), ('deepskyblue', 'deepskyblue'), ('cornflowerblue', 'cornflowerblue'), ('royalblue', 'royalblue'), ('blue', 'blue'), ('steelblue', 'steelblue'), ('navy', 'navy'),  ('darkslateblue', 'darkslateblue'),
        ('lavenderblush', 'lavenderblush'), ('pink', 'pink'), ('plum', 'plum'),  ('violet', 'violet'), ('purple', 'purple'), ('darkorchid', 'darkorchid'), ('indigo', 'indigo'),

    )
    dot_color = models.CharField(default='white', max_length=50, choices = dot_color_choices)
    ax_color_choices = (
        ('white', 'white'), ('whitesmoke', 'whitesmoke'), ('lightgray', 'lightgray'), ('gray', 'gray'), ('dimgray', 'dimgray'), ('black', 'black'),
        ('mistyrose', 'mistyrose'), ('lightcoral', 'lightcoral'), ('coral', 'coral'), ('red', 'red'), ('brown', 'brown'), ('maroon', 'maroon'),
        ('beige', 'beige'), ('yellow', 'yellow'), ('gold', 'gold'), ('orange', 'orange'), ('chocolate', 'chocolate'), ('sienna', 'sienna'),
        ('ivory', 'ivory'), ('lightgreen', 'lightgreen'), ('lime', 'lime'), ('green', 'green'), ('darkgreen', 'darkgreen'), ('olive', 'olive'),
        ('azure', 'azure'), ('aqua', 'aqua'), ('turquoise', 'turquoise'), ('teal', 'teal'), ('darkslategray', 'darkslategray'),
        ('lightblue', 'lightblue'), ('deepskyblue', 'deepskyblue'), ('cornflowerblue', 'cornflowerblue'), ('royalblue', 'royalblue'), ('blue', 'blue'), ('steelblue', 'steelblue'), ('navy', 'navy'), ('darkslateblue', 'darkslateblue'),
        ('lavenderblush', 'lavenderblush'), ('pink', 'pink'), ('plum', 'plum'), ('violet', 'violet'), ('purple', 'purple'), ('darkorchid', 'darkorchid'), ('indigo', 'indigo'),

    )
    ax_color = models.CharField(default='ivory', max_length=50, choices = ax_color_choices)

    c_point_number = models.CharField(default='range(rw.num_points)', max_length=50)
    dot_cmap_choices = (
        ('n', 'kein Farbverlauf'),
        ('tab10', 'tab10'),('tab20', 'tab20'), ('tab20b', 'tab20b'), ('tab20c', 'tab20c'),
        ('Greys', 'Greys'), ('Greens', 'Greens'), ('Blues', 'Blues'), ('Purples', 'Purples'), ('Reds', 'Reds'),  ('Oranges', 'Oranges'), ('Wistia', 'Wistia'),
        ('spring', 'spring'), ('summer', 'summer'), ('autumn', 'autumn'), ('winter', 'winter'),
    )
    dot_cmap = models.CharField(default='Purples', max_length=100, choices = dot_cmap_choices)

    date_added = models.DateTimeField(auto_now_add=True)
    figure = models.ImageField(default='rwvisual/rw_visual', upload_to='rwvisual', blank=True)
    video_n = models.FileField(default='rwvisual/rw_visual_n', upload_to='rwvisual', blank=True)
    video_n2 = models.FileField(default='rwvisual/rw_visual_n2', upload_to='rwvisual', blank=True)
    video_b1 = models.FileField(default='rwvisual/rw_visual_b1', upload_to='rwvisual', blank=True)
    video_b2 = models.FileField(default='rwvisual/rw_visual_b2', upload_to='rwvisual', blank=True)


    def __str__(self):
        """Return a string representation of the model."""
        return self.num_points

