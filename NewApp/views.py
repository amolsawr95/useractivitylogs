from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import NewUser,ActivityPeriod
from .forms import NewUserForm,ActivityPeriodForm
from django.urls import reverse
 
# Create your views here.
#All User Objects
def index(request):
    new_user = NewUser.objects.all()
    return render(request, 'index.html', {'new_user': new_user})

# Create New User

def newuser(request):
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/', messages.success(request, 'User is successfully created.', 'alert-success'))
        else:
            return HttpResponse(form.errors)
    else:
        form = NewUserForm()
        return render(request, 'new.html', {'form': form})

#Create activity

def activity_add (request,id):
    object = get_object_or_404(NewUser, id=id)
    if request.POST:
        form = ActivityPeriodForm(request.POST)
        if form.is_valid():
            inves = form.save(commit=False)
            inves.object = object
            inves.save()
            return HttpResponseRedirect(reverse('activity_log'))
        else:
            return HttpResponse(form.errors)
    else:
        form = ActivityPeriodForm()
        return render(request, 'activityadd.html', {'formtwo': form,'object': object,})



def activity_log(request,id):
    object = get_object_or_404(NewUser, pk=id)
    #Gets all activity objects from id 
    activity = object.activityperiod_set.all()
    return render(request,'activitylog.html',{'object':object,'activity':activity})