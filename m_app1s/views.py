from urllib import request

from django.shortcuts import render, redirect
from .models import Topic
from django.contrib.auth.models import User


def index(request):
    """The home page for Mathe App"""

    return render(request, 'm_app1s/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')

    us = request.user
    context = {'us': us, 'topics': topics}
    return render(request, 'm_app1s/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'm_app1s/topic.html', context)


def impressum(request):
    """Show the impressum."""
    return render(request, 'm_app1s/impressum.html')

