"""emojis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from gifs import views


urlpatterns = [
    path('bobblify/', views.bobblify),
    path('intensify/', views.intensify),
    path('detective/', views.detective),
    path('disappears/', views.disappears),
    path('appears/', views.appears),
    path('carlton_dance/', views.carlton_dance),
    path('rap_battle/', views.rap_battle),
    path('strut/', views.strut),
    path('trapped/', views.trapped),
    path('wrecking-ball/', views.wrecking_ball),
    path('heres-johnny/', views.heres_johnny),
    path('javert/', views.javert),
    path('time/', views.time),
    path('left-hanging/', views.left_hanging),
    path('thinking/', views.thinking),
    path('trump/', views.trump),
    path('hide/', views.hide),
    path('begging/', views.begging),
    path('chimp/', views.chimp),
    path('fire/', views.fire),
    path('computer_kid/', views.computer_kid),
    path('toast/', views.toast),
    path('clapping/', views.clapping),
    path('mind_blown/', views.mind_blown),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
]