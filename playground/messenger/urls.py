from django.urls import path
from .views import ThreadListView,ThreadDetailView

messenger_patterns = ([
    path('',ThreadListView.as_view(),name='list'),
    path('thread/<int:pk>/',ThreadDetailView.as_view(),name='detail'),

],"messenger")