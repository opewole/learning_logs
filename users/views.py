from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register(request):
    """to register a new user"""
    if request.method != "POST":
        # display a blank form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # log the user in and redirect to the home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])

            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    context = {"form": form}
    return render(request, 'registration/register.html', context)


