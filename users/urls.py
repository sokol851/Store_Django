from django.contrib.auth import views
from django.urls import path
from users.views import RegisterView, ProfileUpdateView, ProfileDetailView, ProfileDeleteView, VerifyEmailView, \
    CustomLoginView, UserPasswordResetView, UserPasswordSentView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user_register/', RegisterView.as_view(), name='user_register'),
    path('user_update/<int:pk>', ProfileUpdateView.as_view(), name='user_update'),
    path('user_detail/<int:pk>', ProfileDetailView.as_view(), name='user_detail'),
    path('user_delete/<int:pk>', ProfileDeleteView.as_view(), name='user_delete'),
    path("verify/<token_verify>/", VerifyEmailView.as_view(), name="verify_email"),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('user_password_sent', UserPasswordSentView.as_view(), name='user_password_sent'),
]
