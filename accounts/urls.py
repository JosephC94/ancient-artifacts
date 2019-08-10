from django.conf.urls import url, include
from accounts.views import logout, login, registration
from accounts import urls_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', registration, name='registration'),
    url(r'^password-reset/', include(urls_reset))
    ]