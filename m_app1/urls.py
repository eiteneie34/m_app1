"""m_app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # main url
    path('', include('m_app1s.urls')),
    path('users/', include('users.urls')),
    # decimal number app main url
    path('dnum_show/', include('dnum_show.urls')),
    # random pattern app main url
    path('rw_visual/', include('rw_visual.urls')),
    # physical pendulum app main url
    path('pendulum_show/', include('pendulum_show.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


