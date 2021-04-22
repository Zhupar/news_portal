from django.contrib import admin
from django.urls import path
from .views import NewsList, PostDetail, Search, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name = 'post'),
    path('search/', Search.as_view(), name = 'search'),
    path('add/', PostCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete')
]
