"""artifacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import index, knights_sword, holy_grail, tutankhamun, sandals, excalibur, belt, hammer, lamp
from accounts import urls as accounts_urls
from products import urls as urls_products
from products.views import all_products, place_bid, product_detail, bid_detail
from django.views import static
from .settings import MEDIA_ROOT
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^knights_templar/', knights_sword, name="knights_sword"),
    url(r'^holy_grail/', holy_grail, name="holy_grail"),
    url(r'^tutankhamun/', tutankhamun, name="tutankhamun"),
    url(r'^jesus_sandals/', sandals, name="sandals"),
    url(r'^excalibur/', excalibur, name="excalibur"),
    url(r'^aphrodites_belt/', belt, name="belt"),
    url(r'^thors_hammer/', hammer, name="hammer"),
    url(r'^genies_lamp/', lamp, name="lamp"),
    url(r'^accounts/login/$', index, name='index'),
    url(r'^(?P<pk>\d+)bid_detail/', bid_detail, name='bid_detail'),
    url(r'^(?P<pk>\d+)/product_detail/', product_detail, name="product_detail"),
    url(r'^(?P<pk>\d+)/place_bid/', place_bid, name="place_bid"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]
