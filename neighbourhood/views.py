from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Post, Business

# Create your views here.
@login_required(login_url='/login/')
def index(request):

    neighbourhoods = Neighbourhood.objects.all()
    # contex={
    #     'neighbourhoods':neighbourhoods,
    # }
    return render(request, 'neighbour/index.html', {'neighbourhoods':neighbourhoods})
