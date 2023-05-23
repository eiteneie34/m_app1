from django.urls import path
from . import views

app_name = 'rw_visual'
urlpatterns = [
    
    # the random pattern app, main page url
    path('rw_visual/<int:rw_visual_id>/', views.rw_visual_i, name='rw_visual_i'),
    # random pattern app, new parameters page
    path('rw_visual/<int:rw_visual_id>/new_rw_visual/', views.new_rw_visual, name='new_rw_visual'),
    # random pattern app, animations page
    path('rw_visual/<int:rw_visual_id>/rw_visual_animations/', views.rw_visual_animations,
         name='rw_visual_animations'),
    # random pattern app, animation action
    path('rw_visual/<int:rw_visual_id>/rw_visual_anim_v', views.rw_visual_anim_v,
         name='rw_visual_anim_v'),
    
]
