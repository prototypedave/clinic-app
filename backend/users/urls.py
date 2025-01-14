from django.urls import path

from . import views

urlpatterns = [
    path("admin-registration", views.AdminRegistrationView.as_view(), name='admin-register'),
    path('superuser-check/', views.SuperuserCheckView.as_view(), name='superuser-check'),
    path('login', views.LoginView.as_view(), name='login'),
    path('profile', views.UserProfileView.as_view(), name='profile'),
    path('update-profile-image', views.UpdateProfileImageView.as_view(), name="profile-image"),
]