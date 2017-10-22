from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    url(r'^$', views.lost_search, name='lost_search'),
    url(r'^main/', views.lost_list, name='lost_list'),
    url(r'^update/', views.lost_update, name='lost_update'),
]
