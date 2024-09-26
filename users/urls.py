from django.urls import path
from .views import RegisterView, LogoutView, UserDetailView, UserUpdateView, UserDeleteView, UserListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile-update'),
    path('profile/delete/', UserDeleteView.as_view(), name='profile-delete'),
    path('profile/sellerlist/', UserListView.as_view(), name='user-list'),
]