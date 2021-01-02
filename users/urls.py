""" Define urls for users"""

from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView

app_name = 'users'
urlpatterns = [

#login page
path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
path('logout/', views.logout_view, name='logout'),
path('register/', views.register, name='register'),

]