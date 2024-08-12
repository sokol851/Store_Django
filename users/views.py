from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User

from config import settings


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        self.send_verification_email(user)
        messages.success(
            self.request,
            "Registration successful. Please check your email to verify your account.",
        )
        return response

    @staticmethod
    def send_verification_email(user):
        verification_link = (
            f"{settings.SITE_URL}/users/verify/{user.token_verify}/"
        )
        subject = "Подтвердите регистрацию!"
        message = (f"Благодарим за регистрацию на сайте V-magazine.\n"
                   f"Для активации учётной записи, пожалуйста перейдите по ссылке:\n"
                   f"{verification_link}")
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )


class VerifyEmailView(View):
    def get(self, request, token_verify, *args, **kwargs):
        try:
            user = User.objects.get(token_verify=token_verify)
            user.is_active = True
            user.save()
            message = "Email успешно активирован!"
        except User.DoesNotExist:
            message = "Произошла ошибка. Убедитесь, что переходите по ссылке из письма!"

        return render(request, "users/reg_confirm.html", {"message": message})


class ProfileDetailView(DetailView):
    model = User


class ProfileDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('catalog:index')


class ProfileUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse('users:user_detail', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        user = form.save()
        if user.avatar == '':
            user.avatar = 'users/non_avatar.png'
        user.save()
        return super().form_valid(form)
