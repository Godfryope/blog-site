from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('details/<int:pk>', PostDetailView.as_view(), name='details'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about')
]