from . import views 
from django.urls import path
from django.conf.urls import url



urlpatterns = [
    # path('tutorial/new/', TutorialCreateView.as_view(), name='tutorial-create'),
    # path('', TutorialListView.as_view(), name='index'),
    path('', views.index, name='index'),
]