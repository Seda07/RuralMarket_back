from django.urls import path
from .views import (RegisterView, LogoutView, UserDetailView, UserUpdateView, UserDeleteView, UserListView,
                    CheckUsernameExistsView, CheckEmailExistsView, CheckFirstNameExistsView, )
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register/check-username/', CheckUsernameExistsView.as_view(), name='check-username'),
    path('register/check-email/', CheckEmailExistsView.as_view(), name='check-email'),
    path('register/check-first-name/', CheckFirstNameExistsView.as_view(), name='check-first-name'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile-update'),
    path('profile/delete/', UserDeleteView.as_view(), name='profile-delete'),
    path('profile/sellerlist/', UserListView.as_view(), name='user-list'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]


