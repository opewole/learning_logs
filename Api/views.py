from django.shortcuts import render
from django.http import JsonResponse
from learning_logs.models import Topic, Entry


# Create your views here.


def show_topics_titles(request, user):
    topics = Topic.objects.filter(owner=user).order_by('date_add')
    titles = [topic.text for topic in topics]
    response = {'topics': titles}
    return JsonResponse(response)


def show_topics(request, user):
    entries_from_db = Entry.objects.all().order_by('date_add')
    entries = [entry for entry in entries_from_db if entry.topic.owner == request.user]
    response = dict()
    topics = [entry.topic.text for entry in entries]
    content = [entry.text for entry in entries]
    time = [entry.date_add for entry in entries]
    response.update({'topics': topics, 'entries': content, 'date': time})
    return JsonResponse(response)
