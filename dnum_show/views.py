from django.shortcuts import render, redirect
from m_app1s.models import Topic, Entry
from dnum_show.models import DnumShow
from dnum_show.forms import DnumForm
from dnum_show.dnum_class import DnumNotation, DnumShiftFig
from django.contrib.auth.decorators import login_required


@login_required
def dnum_show_i(request, dnumshow_id):
    """Show a decimal number and its notations ."""
    t = DnumShow.objects.get(id=dnumshow_id)
    dnumDIN, dnumI, dnumS, dnumM, dnumP = "n.a.", 'n.a.', 'n.a.', 'n.a.', 'n.a.'
    dnumMshift, dnumPshift, dnumAbb, dnumPrefix, dnumMinus  = "n.a.", 'n.a.', 'n.a.', 'n.a.', 'n.a.'
    us = str(request.user)
    dnum_fig = "n.a."

    dnumInput = t.dnumInput
    my_dnum = DnumNotation(t.dnumInput, t.precInputDef)
    precInputDef = my_dnum.prec_default()
    my_dnumInput0, my_fminus = my_dnum.dnum_fminus()
    my_mminus = my_dnum.dnum_mminus()
    my_passed = my_dnum.dnum_passed()
    my_dnumInput1 = my_dnum.dnum_lcomma()
    my_dnumInput2 = my_dnum.dnum_fcomma()
    my_dcomma = my_dnum.dnum_dcomma()

    if my_mminus == True or my_passed == False or my_dcomma == True:
        t.dnumDIN, t.dnumI, t.dnumS, t.dnumM, t.dnumP = "n.a.", 'n.a.', 'n.a.', 'n.a.', 'n.a.'
        dnumDIN, dnumI, dnumS, dnumM, dnumP = "Eingabefehler!", 'Eingabefehler!', 'Eingabefehler!', 'n.a.', 'n.a.'
    else:
        my_dnumInput3 = my_dnum.dnum_Irow()

        dnumI = my_dnum.dnum_dnull()
        dnumDIN = my_dnum.dnum_DIN()
        dnumS = my_dnum.scientific_notation()
        dnumM, dnumP = my_dnum.power_notation()

        t.dnumSignum = my_fminus
        t.dnumDIN = dnumDIN
        t.dnumI = dnumI
        t.dnumS = dnumS
        t.dnumM, t.dnumP = dnumM, dnumP
        t.dnumMshift, t.dnumPshift = t.dnumM, t.dnumP
        fminus = t.dnumSignum
        us = str(request.user)
        my_dnumSF = DnumShiftFig(fminus, dnumM, dnumP, us)
        dnumMshift, dnumPshift = my_dnumSF.dnumMshift, my_dnumSF.dnumPshift
        dnumAbb, dnumPrefix = my_dnumSF.prefix()
        t.dnumAbb, t.dnumPrefix = dnumAbb, dnumPrefix
        dnumMinus = my_dnumSF.minus(my_fminus)

        my_dnumSF.dnum_ray()


        dnum_fig = t.photo.url[:23] + '_' + us + '.png'

    ten = '· 10'
    t.save()
    content = {
        'dnumInput': dnumInput,
        'precInputDef': precInputDef,
        'dnumDIN': dnumDIN,
        'dnumI': dnumI,
        'dnumS': dnumS,
        'dnumM': dnumM,
        'dnumP': dnumP,
        'dnumMshift': dnumMshift,
        'dnumPshift': dnumPshift,
        'dnumAbb': dnumAbb,
        'dnumPrefix': dnumPrefix,
        'dnumMinus': dnumMinus,
        'ten': ten,
        'dnum_fig': dnum_fig,
    }
    return render(request, 'dnum_show/dnum_show_i.html', content)


@login_required
def new_dnum(request, dnumshow_id):
    """Add a new  decimal number ."""
    t = DnumShow.objects.get(id=dnumshow_id)
    d = t.entry
    if request.method != 'POST':
        # Keine Daten übermittelt; es wird ein leeres Formular erstellt.
        form = DnumForm(instance=t)
    else:
        # POST-Daten übermittelt; Daten werden verarbeitet.
        form = DnumForm(instance=t, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('dnum_show:dnum_show_i', dnumshow_id)
    # Zeigt ein leeres oder ein als ungültiges erkanntes Formular an.
    context = {'t': t, 'd': d, 'form': form}
    return render(request, 'dnum_show/new_dnum.html', context)


@login_required
def l_shift(request, dnumshow_id):
    """Show a decimal number and its left shift ."""
    t = DnumShow.objects.get(id=dnumshow_id)
    us = str(request.user)
    dnumInput, precInputDef, dnumDIN, dnumI = t.dnumInput, t.precInputDef, t.dnumDIN, t.dnumI
    dnumS, dnumM, dnumP = t.dnumS, t.dnumM, t.dnumP

    my_dnumSF = DnumShiftFig(t.dnumSignum, t.dnumMshift, t.dnumPshift, us)
    my_lrInput = 'l'
    dnumMshift, dnumPshift = my_dnumSF.shift_comma_str(my_lrInput)
    dnumAbb, dnumPrefix = my_dnumSF.prefix()
    t.dnumAbb, t.dnumPrefix = dnumAbb, dnumPrefix
    t.dnumMshift, t.dnumPshift = dnumMshift, dnumPshift
    t.dnumAbb, t.dnumPrefix = dnumAbb, dnumPrefix
    dnumMshift, dnumPshift, dnumAbb, dnumPrefix = t.dnumMshift, t.dnumPshift, t.dnumAbb, t.dnumPrefix
    dnumMinus = my_dnumSF.minus(t.dnumSignum)

    dnum_fig = t.photo.url[:23] + '_' + us + '.png'
    ten = '· 10'
    t.save()
    content = {
        'dnumInput': dnumInput,
        'precInputDef': precInputDef,
        'dnumDIN': dnumDIN,
        'dnumI': dnumI,
        'dnumS': dnumS,
        'dnumM': dnumM,
        'dnumP': dnumP,
        'dnumMshift': dnumMshift,
        'dnumPshift': dnumPshift,
        'dnumAbb': dnumAbb,
        'dnumPrefix': dnumPrefix,
        'dnumMinus': dnumMinus,
        'ten': ten,
        'dnum_fig': dnum_fig,
    }
    return render(request, 'dnum_show/dnum_show_i.html', content)


@login_required
def r_shift(request, dnumshow_id):
    """Show a decimal number and its right show ."""
    t = DnumShow.objects.get(id=dnumshow_id)
    us = str(request.user)
    dnumInput, precInputDef, dnumDIN, dnumI = t.dnumInput, t.precInputDef, t.dnumDIN, t.dnumI
    dnumS, dnumM, dnumP = t.dnumS, t.dnumM, t.dnumP

    my_dnumSF = DnumShiftFig(t.dnumSignum, t.dnumMshift, t.dnumPshift, us)
    my_lrInput = 'r'
    dnumMshift, dnumPshift = my_dnumSF.shift_comma_str(my_lrInput)
    dnumAbb, dnumPrefix = my_dnumSF.prefix()
    t.dnumAbb, t.dnumPrefix = dnumAbb, dnumPrefix
    t.dnumMshift, t.dnumPshift = dnumMshift, dnumPshift
    t.dnumAbb, t.dnumPrefix = dnumAbb, dnumPrefix
    dnumMshift, dnumPshift, dnumAbb, dnumPrefix = t.dnumMshift, t.dnumPshift, t.dnumAbb, t.dnumPrefix
    dnumMinus = my_dnumSF.minus(t.dnumSignum)

    dnum_fig = t.photo.url[:23] + '_' + us + '.png'
    ten = '· 10'
    t.save()
    content = {
        'dnumInput': dnumInput,
        'precInputDef': precInputDef,
        'dnumDIN': dnumDIN,
        'dnumI': dnumI,
        'dnumS': dnumS,
        'dnumM': dnumM,
        'dnumP': dnumP,
        'dnumMshift': dnumMshift,
        'dnumPshift': dnumPshift,
        'dnumAbb': dnumAbb,
        'dnumPrefix': dnumPrefix,
        'dnumMinus': dnumMinus,
        'ten': ten,
        'dnum_fig': dnum_fig,
    }
    return render(request, 'dnum_show/dnum_show_i.html', content)
