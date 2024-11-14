from django.urls import path, reverse_lazy
from django.views.generic import TemplateView

from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView, PasswordResetCompleteView
from users import views


app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('email_confirm/<str:token>/', views.email_confirm, name='email_confirm'),
    path('register_success/', TemplateView.as_view(template_name="users/after_register.html"), name='after_register'),

    path('profile/<int:pk>/', views.MailingUserDetailView.as_view(), name='profile_detail'),
    path('profile/update/<int:pk>/', views.MailingUserUpdateView.as_view(), name='profile_update'),


    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
