from django.urls import path

from .views import *

urlpatterns = [
    path('signup/<membership_id>/',signup_view,name='signup'),
]