"""defini urls patterns for lerning_logs."""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_id>', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),
    path('entry_form/<topic_id>', views.entry_form, name='entry_form'),
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),
    path('edit_topics/<topic_id>', views.edit_topic, name='edit_topic'),
    path('edit_two_entry/<entry_id>', views.edit_two_entry,name='edit_two_entry'),


]
