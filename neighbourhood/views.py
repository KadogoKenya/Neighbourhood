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

def add_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user.profile
            neighbourhood.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'create_neighbourhood.html', {'form': form})
