from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all-meetups'), #our-domains.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail'), #our-domains.com/meetups/<dynamic-path-segment>
]