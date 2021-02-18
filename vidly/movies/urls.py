from . import views
from django.http import path


urlpatterns = [
    path('', views.index, name='index')
]