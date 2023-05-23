from django.db import models
from m_app1s.models import Entry


class PenShow(models.Model):
    """physical pendulum model"""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    alpha_grad_choices = (
        ('10', '10'), ('30', '30'),('45', '45'), ('60', '60'), ('75', '75'), ('90', '90'),
    )
    alpha_grad = models.CharField(default='60', max_length=10, choices=alpha_grad_choices)
    g_choices = (
        ('9.81', '9,81 Erde'), ('1.62', '1,62 Mond'), ('274.00', '274,00 Sonne'), ('3.70', '3,70 Merkur'),
        ('8.87', '8,87 Venus'), ('3.72', '3,72 Mars'), ('24.79', '24,79 Jupiter'), ('10.44', '10,44 Saturn'),
        ('8.87', '8,87 Uranus'), ('11.15', '11,15 Neptun'), ('0.62', '0,62 Pluto'),
        ('0.000167', '0,000167 Komet Tschurjumow-Gerassimenko'),
    )
    g = models.CharField(default='9.98', max_length=10, choices=g_choices)
    l_choices = (
        ('0.5', '50 cm'), ('0.05', '5 cm'), ('0.1', '10 cm'), ('0.25', '25 cm'), ('1.0', '1 m'), ('1.5', '1,5 m'),
        ('2.0', '2 m'), ('5.0', '5 m'), ('10.0', '10 m'), ('20.0', '20 m'),
    )
    l = models.CharField(default='0.25', max_length=10, choices=l_choices)
    m_choices = (
        ('0.2367', '236,7 g Stahlkugel'), ('0.02367', '23,67 g Hartholzkugel'),('0.5744', '574,4 g Urankugel'),
    )
    m = models.CharField(default='0.2367', max_length=10, choices=m_choices)
    rK = models.CharField(default='0.02', max_length=10)
    deltaR_choices = (
        ('0.09', 'Luftwiderstand-Koeffizient bei dem normalen Luftdruck'),
        ('0.0009', 'Luftwiderstand-Koeffizient bei dem sehr kleinen Luftdruck'),
        ('0.009', 'Luftwiderstand-Koeffizient bei dem kleinen Luftdruck'),
        ('0.9', 'Luftwiderstand-Koeffizient bei dem großen Luftdruck'),
        ('9.0', 'Luftwiderstand-Koeffizient bei dem sehr großen Luftdruck'),
    )
    deltaR = models.CharField(default='0.07', max_length=10, choices=deltaR_choices)
    anzahlT_choices = (
        ('1', '1'), ('2', '2'),('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
    )

    anzahlT = models.CharField(default='3', max_length=10, choices = anzahlT_choices)
    x_max = models.CharField(default='3.1', max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)
    mk_animv = models.BooleanField(default=False)
    mk_animx = models.BooleanField(default=False)


    figure = models.ImageField(default='pendulum/pen_show', upload_to='pendulum', blank=True)
    #video_t = models.FileField(default='pendulum/anim_t', upload_to='pendulum', blank=True)
    video_v = models.FileField(default='pendulum/anim_v', upload_to='pendulum', blank=True)
    video_x = models.FileField(default='pendulum/anim_x', upload_to='pendulum', blank=True)
    video_a = models.FileField(default='pendulum/anim_a', upload_to='pendulum', blank=True)
    video_b = models.FileField(default='pendulum/anim_b', upload_to='pendulum', blank=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.alpha_grad

