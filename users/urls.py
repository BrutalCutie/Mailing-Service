from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users import views


app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('profile/<int:pk>/', views.MailingUserDetailView.as_view(), name='profile_detail'),
    path('profile/update/<int:pk>/', views.MailingUserUpdateView.as_view(), name='profile_update'),
]
