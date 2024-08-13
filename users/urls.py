from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.views import RegisterView, ProfileUpdateView, ProfileDetailView, ProfileDeleteView, VerifyEmailView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_register/', RegisterView.as_view(), name='user_register'),
    path('user_update/<int:pk>', ProfileUpdateView.as_view(), name='user_update'),
    path('user_detail/<int:pk>', ProfileDetailView.as_view(), name='user_detail'),
    path('user_delete/<int:pk>', ProfileDeleteView.as_view(), name='user_delete'),
    path("verify/<token_verify>/", VerifyEmailView.as_view(), name="verify_email"),
]
