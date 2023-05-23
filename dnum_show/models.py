from django.db import models
from m_app1s.models import Entry


class DnumShow(models.Model):
    """A decimal number notation model."""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    dnumInput = models.CharField(default='0,0001', max_length=50)
    precInputDef = models.CharField(default=4, max_length=2)
    dnumDIN = models.CharField(default='n.a.', max_length=50)
    dnumI = models.CharField(default='n.a.', max_length=50)
    dnumS = models.CharField(default='n.a.', max_length=100)
    dnumM = models.CharField(default='n.a.', max_length=50)
    dnumP = models.CharField(default='n.a.', max_length=10)
    dnumMshift = models.CharField(default='n.a.', max_length=50)
    dnumPshift = models.CharField(default='n.a.', max_length=10)
    dnumSignum = models.BooleanField(default=False)
    dnumAbb = models.CharField(default='n.a.', max_length=4)
    dnumPrefix = models.CharField(default='n.a.', max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default='dnumray/dnum_ray', upload_to='dnumray', blank=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.dnumInput
