from django.urls import path
from . import views

urlpatterns = [
    path('login_page', views.login_page, name='login'),
    path('logout_page', views.logout_user, name='logout'),
    path('signup_page', views.signup_page, name='signup'),
    path('edit_profile_page', views.edit_profile_page, name='edit_profile')
]