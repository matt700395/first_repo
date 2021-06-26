from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView, index, ArticleListIndexView


app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
    path('list_index/', ArticleListIndexView.as_view(), name='list_index'),

    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    url(r'^index/$', index, name='index')

]