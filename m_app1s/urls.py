from django.urls import path
from . import views

app_name = 'm_app1s'
urlpatterns = [
    #   home page url
    path('', views.index, name='index'),
    #   topics page url
    path('topics/', views.topics, name='topics'),
    #   topic page url
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #  page impressum
    path('impressum/', views.impressum, name='impressum'),

]
