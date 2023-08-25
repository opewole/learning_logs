"""defini urls patterns for lerning_logs."""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('get/topics_titles/<user>', views.show_topics_titles, name='api_topics_titles'),
    path('get/topics/user=<user>', views.show_topics, name='api_topics_full'),

]