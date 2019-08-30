from django.conf.urls import url, include
from home.views import knights_sword, holy_grail, tutankhamun, sandals, excalibur, belt, hammer, lamp, index
from accounts import urls_reset

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^accounts/login/$', index, name='index'),
    url(r'^knights_templar/', knights_sword, name="knights_sword"),
    url(r'^holy_grail/', holy_grail, name="holy_grail"),
    url(r'^tutankhamun/', tutankhamun, name="tutankhamun"),
    url(r'^jesus_sandals/', sandals, name="sandals"),
    url(r'^excalibur/', excalibur, name="excalibur"),
    url(r'^aphrodites_belt/', belt, name="belt"),
    url(r'^thors_hammer/', hammer, name="hammer"),
    url(r'^genies_lamp/', lamp, name="lamp"),
    ]