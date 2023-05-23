from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Zeigt das leere Registrierungsformular an.
        form = UserCreationForm()
    else:
        # Verarbeitet das ausgefüllte Formular.
        form = UserCreationForm(data=request.POST)


        if form.is_valid():
            new_user = form.save()
            # Meldet den Benutzer an und leitet ihn zur Startseite.
            login(request, new_user)
            return redirect('m_app1s:index')

    # Zeigt ein leeres oder ein als ungültig erkanntes Formular an.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
