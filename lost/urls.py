from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lost_search, name='lost_search'),
    url(r'^main/', views.lost_list, name='lost_list'),
]