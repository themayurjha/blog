from django.urls import path
from .views import UserCreateView
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostListView, PostDetailView


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
