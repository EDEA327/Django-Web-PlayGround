from django.urls import path
from .views import ThreadListView,ThreadDetailView,add_message

messenger_patterns = ([
    path('',ThreadListView.as_view(),name='list'),
    path('thread/<int:pk>/',ThreadDetailView.as_view(),name='detail'),
    path('thread/<int:pk>/add/',add_message,name='add'),

],"messenger")