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


@login_required(login_url='login')
def all_neighbourhoods(request):
    neighbourhoods = Neighbourhood.objects.all()
    neighbourhoods = mitaa_zote[::-1]
    context = {
        'neighbourhoods': neighbourhoods,
    }
    return render(request, 'all_neighbourhoods.html', context)


def new_posts(request, neighbour_id):
    neighbour = Neighbourhood.objects.get(id=mtaa_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighbour = neighbour
            post.user = request.user
            post.save()
            return redirect('neighbour', neighbour.id)
    else:
        form = PostForm()
    return render(request, 'new_posts.html', {'form': form})



def neighbour(request, neighbour_id):
    neighbour = Neighbourhood.objects.get(id=neighbour_id)
    business = Business.objects.filter(id=neighbour_id)
    posts = Post.objects.filter(id=neighbour_id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = neighbour
            b_form.user = request.user
            b_form.save()
            return redirect('neighbour', neighbour.id)
    else:
        form = BusinessForm()

    
    context = {
        'neighbour': neighbour,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'neighbour.html', context)
