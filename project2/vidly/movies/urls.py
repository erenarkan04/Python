from django.conf.urls import url, include
from . import views
from django.urls import

urlpatterns = [
    url('', views.index(), name='index')
]
