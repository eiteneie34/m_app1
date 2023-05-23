from django.urls import path
from . import views

app_name = 'pendulum_show'
urlpatterns = [
    
    # physical pendulum app, main page
    path('pendulum_show/<int:pendulum_show_id>/', views.pendulum_show_i, name='pendulum_show_i'),

    # physical pendulum app, new parameters page
    path('pendulum_show/<int:pendulum_show_id>/new_pendulum_show/', views.new_pendulum_show, name='new_pendulum_show'),
    # physical pendulum app, animations page
    path('pendulum_show/<int:pendulum_show_id>/pendulum_show_animations/', views.pendulum_show_animations,
         name='pendulum_show_animations'),
    # physical pendulum app, animation t window
    path('pendulum_show/<int:pendulum_show_id>/pendulum_show_anim_v', views.pendulum_show_anim_v,
         name='pendulum_show_anim_v'),
    # physical pendulum app, animation x window
    path('pendulum_show/<int:pendulum_show_id>/pendulum_show_anim_x', views.pendulum_show_anim_x,
         name='pendulum_show_anim_x'),


]
