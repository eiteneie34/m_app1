from django.shortcuts import render, redirect
from m_app1s.models import Topic, Entry
from rw_visual.models import RwVisual
from rw_visual.random_walk_class import RandomFigure, RandomFigureAnim
from rw_visual.forms import RwVisualForm
from django.contrib.auth.decorators import login_required


@login_required
def rw_visual_i(request, rw_visual_id):
    """Show the random pattern app and its parameters."""
    t = RwVisual.objects.get(id=rw_visual_id)
    num_points = int(t.num_points)
    x_distance_str = t.x_distance
    y_distance_str = t.y_distance

    dot_marker = t.dot_marker
    dot_size = t.dot_size
    dot_size_v = t.dot_size_v
    dot_color = t.dot_color
    dot_alpha = t.dot_alpha
    dot_alpha_v = t.dot_alpha_v
    dot_cmap = t.dot_cmap
    ax_color = t.ax_color
    us = str(request.user)
    mk_anim = False
    mk_anim_pr = False
    num_points_i = False

    my_fig = RandomFigure(num_points, x_distance_str, y_distance_str,  us)
    x_values, y_values, point_numbers_random = my_fig.fill_walk()
    t.x_values, t.y_values, t.point_numbers_random = x_values, y_values, point_numbers_random
    t.save()
    num_points_soll = int(2500)
    if int(num_points) <= num_points_soll:
        num_points_i = 'True'

    my_fig.rw_figure(
        dot_marker=dot_marker,
        dot_size=int(dot_size),
        dot_size_v=dot_size_v,
        dot_color=dot_color,
        dot_alpha=float(dot_alpha),
        dot_alpha_v=dot_alpha_v,
        dot_cmap=dot_cmap,
        ax_color=ax_color
    )
    dot_marker_labs = {
        '.': 'Punkt', 'o': 'Kreis', 's': 'Quadrat', '^': 'Dreieck ^', 'v': 'Dreieck v',
        '8': 'Octagon', 'D': 'Diamant', 'd': 'Rombe', 'p': 'Pentagon', 'H': 'Hexagon',
        '(4,1)': 'Stern 4', '*': 'Stern 5',  '(7,1)': 'Stern 7', '(8,1)': 'Stern 8', '(9,1)': 'Stern 9',
        '(5,2)': 'Schneeflocke 5', '(6,2)': 'Schneeflocke 6', '(7,2)': 'Schneeflocke 7',
        '(8,2)': 'Schneeflocke 8', '(9,2)': 'Schneeflocke 9',
    }
    for dot_marker_key, dot_marker_lab in dot_marker_labs.items():
        if dot_marker_key == dot_marker:
            dot_marker_label = dot_marker_lab

    dot_cmap_label = dot_cmap
    if  dot_cmap=='n':
        dot_cmap_label='kein Farbverlauf'

    rwvisual = t.figure.url[:25] + '_' + us + '.png'
    num_points_soll = int(2500)
    if int(t.num_points) <= num_points_soll:
        num_points_i = True
    content = {
        'num_points': num_points,
        'num_points_i': num_points_i,
        'x_distance_str': x_distance_str,
        'y_distance_str': y_distance_str,
        'dot_marker_label': dot_marker_label,
        'dot_size': dot_size,
        'dot_color': dot_color,
        'dot_alpha': dot_alpha,
        'dot_cmap_label': dot_cmap_label,
        'ax_color': ax_color,
        'rwvisual': rwvisual,
        'mk_anim': mk_anim,
        'mk_anim_pr': mk_anim_pr,

    }
    return render(request, 'rw_visual/rw_visual_i.html', content)


@login_required
def rw_visual_anim_v(request, rw_visual_id):
    """Show the random pattern app and its parameters."""
    mk_anim_pr = True
    t = RwVisual.objects.get(id=rw_visual_id)
    num_points = int(t.num_points)
    x_values_str, y_values_str, point_numbers_random_str = t.x_values, t.y_values, t.point_numbers_random
    dot_marker = t.dot_marker
    dot_size = t.dot_size
    dot_color = t.dot_color
    dot_alpha = t.dot_alpha
    dot_cmap = t.dot_cmap
    ax_color = t.ax_color
    us = str(request.user)
    x_distance_str, y_distance_str = t.x_distance, t.y_distance
    dot_size_v, dot_alpha_v = t.dot_size_v, t.dot_alpha_v
    my_fig_a = RandomFigureAnim(num_points, x_distance_str, y_distance_str, point_numbers_random_str, x_values_str, y_values_str, us)
    #my_fig_a.fill_walk()
    #my_fig_a.ran_fig_anim(
        #dot_marker=dot_marker,
        #dot_size=float(dot_size),
        #dot_size_v = dot_size_v,
        #dot_color=dot_color,
        #dot_alpha=float(dot_alpha),
        #dot_alpha_v=dot_alpha_v,
        #dot_cmap=dot_cmap,
        #ax_color=ax_color
    #)

    pr = my_fig_a.ran_fig_anim2(
            dot_marker=dot_marker,
            dot_size=int(dot_size),
            dot_size_v=dot_size_v,
            dot_color=dot_color,
            dot_alpha=float(dot_alpha),
            dot_alpha_v=dot_alpha_v,
            dot_cmap=dot_cmap,
            ax_color=ax_color
        )
    dot_marker_labs = {
        '.': 'Punkt', 'o': 'Kreis', 's': 'Quadrat', '^': 'Dreieck ^', 'v': 'Dreieck v',
        '8': 'Octagon', 'D': 'Diamant', 'd': 'Rombe', 'p': 'Pentagon', 'H': 'Hexagon',
        '(4,1)': 'Stern 4', '*': 'Stern 5', '(7,1)': 'Stern 7', '(8,1)': 'Stern 8', '(9,1)': 'Stern 9',
        '(5,2)': 'Schneeflocke 5', '(6,2)': 'Schneeflocke 6', '(7,2)': 'Schneeflocke 7',
        '(8,2)': 'Schneeflocke 8', '(9,2)': 'Schneeflocke 9',
    }
    for dot_marker_key, dot_marker_lab in dot_marker_labs.items():
        if dot_marker_key == dot_marker:
            dot_marker_label = dot_marker_lab

    dot_cmap_label = dot_cmap
    if  dot_cmap=='n':
        dot_cmap_label='kein Farbverlauf'

    mk_anim = True
    if pr == False:
        mk_anim_pr = False
    rwvisual = t.figure.url[:25] + '_' + us + '.png'

    content = {
        'num_points': num_points,

        'x_distance_str': x_distance_str,
        'y_distance_str': y_distance_str,
        'dot_marker_label': dot_marker_label,
        'dot_size': dot_size,
        'dot_color': dot_color,
        'dot_alpha': dot_alpha,
        'dot_cmap_label': dot_cmap_label,
        'ax_color': ax_color,
        'rwvisual': rwvisual,
        'mk_anim': mk_anim,
        'mk_anim_pr': mk_anim_pr,



    }
    return render(request, 'rw_visual/rw_visual_i.html', content)


@login_required
def rw_visual_animations(request, rw_visual_id):
    """Show the random pattern app and its parameters."""
    t = RwVisual.objects.get(id=rw_visual_id)
    num_points = int(t.num_points)
    dot_marker = t.dot_marker
    dot_size = t.dot_size
    dot_color = t.dot_color
    dot_alpha = t.dot_alpha
    dot_cmap = t.dot_cmap
    ax_color = t.ax_color
    us = str(request.user)



    dot_marker_labs = {
        '.': 'Punkt', 'o': 'Kreis', 's': 'Quadrat', '^': 'Dreieck ^', 'v': 'Dreieck v',
        '8': 'Octagon', 'D': 'Diamant', 'd': 'Rombe',  'p': 'Pentagon', 'H': 'Hexagon',
        '(4,1)': 'Stern 4', '*': 'Stern 5', '(7,1)': 'Stern 7', '(8,1)': 'Stern 8', '(9,1)': 'Stern 9',
        '(5,2)': 'Schneeflocke 5', '(6,2)': 'Schneeflocke 6', '(7,2)': 'Schneeflocke 7',
        '(8,2)': 'Schneeflocke 8', '(9,2)': 'Schneeflocke 9',
    }
    for dot_marker_key, dot_marker_lab in dot_marker_labs.items():
        if dot_marker_key == dot_marker:
            dot_marker_label = dot_marker_lab

    dot_cmap_label = dot_cmap
    if  dot_cmap=='n':
        dot_cmap_label='kein Farbverlauf'

    #rw_vid_n = t.video_n.url[:27] + '_' + us + '.mp4'
    rw_vid_n2 = t.video_n2.url[:28] + '_' + us + '.mp4'
    rw_vid_b1 = t.video_b1.url[:28] + '.mp4'
    rw_vid_b2 = t.video_b2.url[:28] + '_stern_tab20' + '.mp4'
    rwvisual = t.figure.url[:25] + '_' + us + '.png'

    content = {
        'num_points': num_points,

        'dot_marker_label': dot_marker_label,
        'dot_size': dot_size,
        'dot_color': dot_color,
        'dot_alpha': dot_alpha,
        'dot_cmap_label': dot_cmap_label,
        'ax_color': ax_color,
        #'rw_vid_n': rw_vid_n,
        'rw_vid_n2': rw_vid_n2,
        'rw_vid_b1': rw_vid_b1,
        'rw_vid_b2': rw_vid_b2,
        'rwvisual': rwvisual,
    }
    return render(request, 'rw_visual/rw_visual_animations.html', content)



@login_required
def new_rw_visual(request, rw_visual_id):
    """Add a new parameters to the random pattern app."""
    t = RwVisual.objects.get(id=rw_visual_id)
    d = t.entry
    if request.method != 'POST':
        # Keine Daten übermittelt; es wird ein leeres Formular erstellt.
        form = RwVisualForm(instance=t)
    else:
        # POST-Daten übermittelt; Daten werden verarbeitet.
        form = RwVisualForm(instance=t, data=request.POST)

        if form.is_valid():

            form.save()

            return redirect('rw_visual:rw_visual_i', rw_visual_id)

    # Zeigt ein leeres oder ein als ungültiges erkanntes Formular an.
    context = {'t': t, 'd': d, 'form': form}
    return render(request, 'rw_visual/new_rw_visual.html', context)


