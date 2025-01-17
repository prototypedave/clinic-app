from django.urls import path

from . import views

urlpatterns = [
    path("admin-registration", views.AdminRegistrationView.as_view(), name='admin-register'),
    path('superuser-check/', views.SuperuserCheckView.as_view(), name='superuser-check'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('profile', views.UserProfileView.as_view(), name='profile'),
    path('update-profile-image', views.UpdateProfileImageView.as_view(), name="update-profile-image"),
    path('send-link', views.SendResetLinkView.as_view(), name="reset-link"),
    path('validate-token/<uuid:token>/', views.ResetTokenValidationView.as_view(), name="token-validation"),
    path('valid', views.ValidView.as_view(), name='valid'),
    path('password-reset/<str:token>/', views.PasswordResetView.as_view, name='password-change')
]