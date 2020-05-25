from django.shortcuts import render,redirect

from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponseRedirect
from rest_framework import filters
from django.db.models import Q
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'poll/index.html',{})


def home(request):
    return redirect('search')


def create(request):
    if request.method == 'POST':
        form=CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')
    else:
        form=CreatePollForm()
    context = {
        'form' : form,
    }
    return render(request, 'poll/create.html', context)

def search(request):
    if request.method=='POST':
        srch=request.POST['srh']

        if srch:
            match=Poll.objects.filter(Q(question__icontains=srch))
            if match:
                return render(request,'poll/search.html',{'sr':match})
            else:
                messages.error(request,'no results found')
        else:
            return HttpResponseRedirect('/search/')
    return render(request,'poll/search.html')



