from django.conf.urls import url
from apprest import views


urlpatterns = [
    url(r'^apprest/$', views.libro_list),
    url(r'^apprest/(?P<pk>[0-9]+)/$', views.libro_detail),
]
