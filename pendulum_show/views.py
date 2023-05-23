from django.shortcuts import render, redirect

from m_app1s.models import Topic, Entry
from pendulum_show.models import PenShow
from pendulum_show.pendulum_class import PendulumFig, PendulumFigAnim
from pendulum_show.forms import PenShowForm
from django.contrib.auth.decorators import login_required


@login_required
def pendulum_show_i(request, pendulum_show_id):
    """Show a physical pendulum and its parameters ."""
    t = PenShow.objects.get(id=pendulum_show_id)
    alpha_grad = float(t.alpha_grad)
    g = float(t.g)
    l = float(t.l)
    m = float(t.m)
    rK = float(t.rK)
    deltaR = float(t.deltaR)
    anzahlT = int(t.anzahlT)
    us = str(request.user)
    mk_animv, mk_animx = False, False
    t.mk_animv, t.mk_animx = mk_animv, mk_animx


    my_pf = PendulumFig(alpha_grad, g, l, m, rK, deltaR, anzahlT, us)
    my_pf.p_steps()
    my_pf.p_arrays()
    my_pf.p_calc()
    x_max = my_pf.p_fig_t()
    t.x_max = x_max
    pn_fig = t.figure.url[:24] + '_' + us + '.png'
    t.save()
    mk_animv, mk_animx = t.mk_animv, t.mk_animx
    x_max_i = False
    x_max_soll = 3.1
    if float(t.x_max) <= x_max_soll:
        x_max_i = True
    content = {
        'alpha_grad': alpha_grad,
        'g': g,
        'l': l,
        'm': m,
        'rK': rK,
        'deltaR': deltaR,
        'anzahlT': anzahlT,
        'x_max_i': x_max_i,
        'us': us,
        'pn_fig': pn_fig,
        'mk_animv': mk_animv, 'mk_animx': mk_animx,


    }
    return render(request, 'pendulum_show/pendulum_show_i.html', content)


@login_required
def pendulum_show_anim_v(request, pendulum_show_id):
    """ Show the animations of the physical pendulum."""

    t = PenShow.objects.get(id=pendulum_show_id)
    alpha_grad = float(t.alpha_grad)
    g = float(t.g)
    l = float(t.l)
    m = float(t.m)
    rK = float(t.rK)
    deltaR = float(t.deltaR)
    anzahlT = int(t.anzahlT)
    us = str(request.user)
    mk_animv, mk_animx = t.mk_animv, t.mk_animx

    my_pa = PendulumFigAnim(alpha_grad, g, l, m, rK, deltaR, anzahlT, us)
    my_pa.p_steps()
    my_pa.p_arrays()
    my_pa.p_calc()
    prv = my_pa.p_fig_t_anim()


    if prv == False:
        mk_animv = True
    t.mk_animv = mk_animv
    t.save()
    mk_animv, mk_animx = t.mk_animv, t.mk_animx
    x_max_i = False
    x_max_soll = 3.1
    if float(t.x_max) <= x_max_soll:
        x_max_i = True
    pn_fig = t.figure.url[:24] + '_' + us + '.png'
    content = {
        'us': us,
        'alpha_grad': alpha_grad,
        'g': g,
        'l': l,
        'm': m,
        'rK': rK,
        'deltaR': deltaR,
        'anzahlT': anzahlT,
        'x_max_i': x_max_i,
        'pn_fig': pn_fig,
        'mk_animv': mk_animv, 'mk_animx': mk_animx,


    }
    return render(request, 'pendulum_show/pendulum_show_i.html', content)


@login_required
def pendulum_show_anim_x(request, pendulum_show_id):
    """ Show the animations of the physical pendulum."""
    t = PenShow.objects.get(id=pendulum_show_id)
    alpha_grad = float(t.alpha_grad)
    g = float(t.g)
    l = float(t.l)
    m = float(t.m)
    rK = float(t.rK)
    deltaR = float(t.deltaR)
    anzahlT = int(t.anzahlT)
    us = str(request.user)
    mk_animv, mk_animx = t.mk_animv, t.mk_animx

    my_pap = PendulumFigAnim(alpha_grad, g, l, m, rK, deltaR, anzahlT, us)
    my_pap.p_steps()
    my_pap.p_arrays()
    my_pap.p_calc()
    prx = my_pap.p_polar_fig_anim()

    if prx==False:
        mk_animx = True
    t.mk_animx = mk_animx
    t.save()
    mk_animv, mk_animx = t.mk_animv, t.mk_animx
    x_max_i = False
    x_max_soll = 3.1
    if float(t.x_max) <= x_max_soll:
        x_max_i = True
    pn_fig = t.figure.url[:24] + '_' + us + '.png'
    content = {
        'us': us,
        'alpha_grad': alpha_grad,
        'g': g,
        'l': l,
        'm': m,
        'rK': rK,
        'deltaR': deltaR,
        'anzahlT': anzahlT,
        'x_max_i': x_max_i,
        'pn_fig': pn_fig,
        'mk_animv': mk_animv, 'mk_animx': mk_animx,

    }
    return render(request, 'pendulum_show/pendulum_show_i.html', content)


@login_required
def pendulum_show_animations(request, pendulum_show_id):
    """ Show the animations of the physical pendulum."""
    t = PenShow.objects.get(id=pendulum_show_id)
    alpha_grad = float(t.alpha_grad)
    g = float(t.g)
    l = float(t.l)
    m = float(t.m)
    rK = float(t.rK)
    deltaR = float(t.deltaR)
    anzahlT = int(t.anzahlT)
    us = str(request.user)


    pn_vid_v = t.video_v.url[:22] + '_' + us + '.mp4'
    pn_vid_x = t.video_x.url[:22] + '_' + us + '.mp4'
    pn_vid_a = t.video_a.url[:22] + '.mp4'
    pn_vid_b = t.video_b.url[:22] + '.mp4'
    content = {
        'us': us,
        'alpha_grad': alpha_grad,
        'g': g,
        'l': l,
        'm': m,
        'rK': rK,
        'deltaR': deltaR,
        'anzahlT': anzahlT,
        'pn_vid_v': pn_vid_v,
        'pn_vid_x': pn_vid_x,
        'pn_vid_a': pn_vid_a,
        'pn_vid_b': pn_vid_b,
    }
    return render(request, 'pendulum_show/pendulum_show_animations.html', content)


@login_required
def new_pendulum_show(request, pendulum_show_id):
    """Add a new parameters of the physical pendulum."""
    t = PenShow.objects.get(id=pendulum_show_id)
    d = t.entry
    if request.method != 'POST':
        # Keine Daten übermittelt; es wird ein leeres Formular erstellt.
        form = PenShowForm(instance=t)
    else:
        # POST-Daten übermittelt; Daten werden verarbeitet.
        form = PenShowForm(instance=t, data=request.POST)

        if form.is_valid():

            form.save()

            return redirect('pendulum_show:pendulum_show_i', pendulum_show_id)

    # Zeigt ein leeres oder ein als ungültiges erkanntes Formular an.
    context = {'t': t, 'd': d, 'form': form}
    return render(request, 'pendulum_show/new_pendulum_show.html', context)


