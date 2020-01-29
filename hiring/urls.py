from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candidate_list/', views.candidate_list, name='candidate_list'),
    url(r'candidate/(?P<pk>\d+)/$', views.track_status, name='track_status')
]
