from django.urls import path
from .views import PageListView,PageDetailView
from . import views

urlpatterns = [
    path('',PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
]