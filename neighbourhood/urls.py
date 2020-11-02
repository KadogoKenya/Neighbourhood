from . import views 
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('tutorial/new/', TutorialCreateView.as_view(), name='tutorial-create'),
    # path('', TutorialListView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('add_neighbourhood/', views.add_neighbourhood, name='add_neighbourhood'),
]