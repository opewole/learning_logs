from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # HOME PAGE
    path('login', LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]
