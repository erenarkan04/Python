from . import views
from django.http import path
from

urlpatterns = [
    path('', views.index, name='index')
]