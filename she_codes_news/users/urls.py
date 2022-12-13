from django.urls import path
from .views import CreateAccountView, EditAccountView, ProfileView, PasswordsChangeView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
name='createAccount'),
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/edit', EditAccountView.as_view(), name='editAccount'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
]

