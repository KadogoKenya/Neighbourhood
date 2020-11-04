from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Post, Business
from .forms import NeighbourHoodForm, PostForm, BusinessForm
from django.views.generic.edit import DeleteView

# Create your views here.
@login_required(login_url='/login/')
def index(request):

    neighbourhoods = Neighbourhood.objects.all()
    # contex={
    #     'neighbourhoods':neighbourhoods,
    # }
    return render(request, 'neighbour/index.html', {'neighbourhoods':neighbourhoods})


@login_required(login_url='login')
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
    neighbourhoods = neighbourhoods[::-1]
    context = {
        'neighbourhoods': neighbourhoods,
    }
    return render(request, 'all_neighbourhoods.html', context)

@login_required(login_url='login')
def new_posts(request, neighbour_id):
    neighbour = Neighbourhood.objects.get(id=neighbour_id)
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


@login_required(login_url='login')
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


def search_by_name(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'neighbour/search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'neighbour/search.html',{"message":message})


def delete_view(request, neighbour_id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={
        'neighbour': neighbour,
    } 
  
    # fetch the object related to passed id 
    neighbour = get_object_or_404(Neighbourhood, id = neighbour_id) 
  
  
    if request.method =="POST": 
        # delete object 
        neighbour.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/") 
  
    return render(request, "delete_view.html", context) 

# class NeighbourhoodDeleteView(DeleteView): 
    
#     model = Neighbourhood

#     success_url ="/"
