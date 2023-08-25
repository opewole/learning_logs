from django.shortcuts import render, get_object_or_404
from learning_logs.models import Topic, Entry
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from learning_logs.forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """The home page of learning log """
    # return HttpResponse("<b>lets start with this</b>sss")
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    # topics = Topic.objects.all().order_by('date_add')
    topics = Topic.objects.filter(owner=request.user).order_by('date_add')
    context = {'topic': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    #topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if request.user != topic.owner:
        raise Http404
    entries = topic.entry_set.order_by('date_add')
    context = {'topic': topic, 'entries': entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # no data submitted, display blank form instead
        form = TopicForm
    else:
        # process the form and save it
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def entry_form(request, topic_id):
    #topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    context = {'topic': topic}
    if request.method == 'POST':
        text = request.POST['text']

        entry = Entry(text=text, topic=topic)

        if entry:
            entry.save()

            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    return render(request, "learning_logs/entry_form.html", context)


@login_required
def edit_entry(request, entry_id):
    #entry = Entry.objects.get(id=entry_id)
    entry = get_object_or_404(Entry, id=entry_id)
    context = {'entry': entry}

    if request.method == 'POST':
        text = request.POST['text']
        entry.text = text

        if entry:
            entry.save()
            return HttpResponseRedirect(reverse('topic', args=[entry.topic.id]))

    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def edit_topic(request, topic_id):
    #topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    context = {'topic': topic}
    if request.method == 'POST':
        text = request.POST['text']
        topic.text = text

        if topic:
            topic.save()
            return HttpResponseRedirect(reverse('topics'))

    return render(request, 'learning_logs/edit_topic.html', context)


@login_required
def new_entry(request, topic_id):
    #topic = Topic.objects.get(id=topic_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_two_entry(request, entry_id):
    #entry_to_edit = Entry.objects.get(id=entry_id)
    entry_to_edit = get_object_or_404(Topic, id=entry_id)
    if request.user != edit_two_entry.topic.owner:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry_to_edit)
    else:
        form = EntryForm(instance=entry_to_edit, data=request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[entry_to_edit.topic.id]))
    context = {'entry': entry_to_edit, 'form': form}
    return render(request, "learning_logs/edit_two_entry.html", context)


