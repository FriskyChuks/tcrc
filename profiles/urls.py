from django.urls import path

from .views import *

urlpatterns = [
    path('membership/', membership_registration_view, name='membership'),
    path('activate_user/<id>/', activate_user_view, name='activate_user'),
    path('deactivate_user/<id>/', deactivate_user_view, name='deactivate_user'),
    path('login_view/', login_view, name='login'),
    path('logout_view/', logout_view, name='logout'),
    path('search/', search_user, name='search'),
    path('update_user_view/<id>/', update_user_view, name='update_user'),
]
