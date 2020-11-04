from . import views 
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from .views import NeighbourhoodDeleteView 



urlpatterns = [
    # path('tutorial/new/', TutorialCreateView.as_view(), name='tutorial-create'),
    # path('', TutorialListView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('create_neighbourhood', views.add_neighbourhood, name='create_neighbourhood'),
    path('', views.index, name='index'),
    path('all_neighbourhoods', views.all_neighbourhoods, name='all_neighbourhoods'),
    path('new_posts/<neighbour_id>', views.new_posts, name='new_posts'),
    path('neighbour/<neighbour_id>', views.neighbour, name='neighbour'),
    url(r'^search/', views.search_by_name, name='search_results'),
    path('<id>/delete', views.delete_view, name='delete_view'),
    # path('<pk>/delete/', NeighbourhoodDeleteView.as_view()), 


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)