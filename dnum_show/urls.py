from django.urls import path
from . import views

app_name = 'dnum_show'
urlpatterns = [
    
    # decimal number notation, main page url
    path('dnum_show/<int:dnumshow_id>/', views.dnum_show_i, name='dnum_show_i'),
    # decimal number notation, new page url
    path('new_dnum/<int:dnumshow_id>/', views.new_dnum, name='new_dnum'),
    # decimal number notation, left shift page url
    path('dnum_show/<int:dnumshow_id>/l_shift', views.l_shift, name='l_shift'),
    # decimal number notation, right shift page url
    path('dnum_show/<int:dnumshow_id>/r_shift', views.r_shift, name='r_shift'),
    
]
