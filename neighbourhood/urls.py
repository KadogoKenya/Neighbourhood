from . import views 
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('tutorial/new/', TutorialCreateView.as_view(), name='tutorial-create'),
    # path('', TutorialListView.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('', views.add_neighbourhood, name='create_neighbourhood'),
    path('index', views.index, name='index'),

    path('all_neighbourhoods/', views.all_neighbourhoods, name='all_neighbourhoods'),

    path('new_posts/<neighbour_id>', views.add_neighbourhood, name='new_posts'),

    path('neighbour/<neighbour_id>', views.add_neighbourhood, name='neighbour'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)