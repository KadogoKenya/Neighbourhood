from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from users.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):

    neighbourhood = Neighbourhood.objects.all()
    contex={
        'neighbourhoods':neighbourhoods,
    }
    return render(request, 'neighbour/index.html', context)
