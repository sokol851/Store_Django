from config import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user.is_active = False
    #     user.save()
    #
    #     token = default_token_generator.make_token(user)
    #     uid = urlsafe_base64_encode(force_bytes(user.pk))
    #     activation_url = reverse_lazy('users:reg_done', kwargs={'uidb64': uid, 'token': token})
    #
    #     send_mail(
    #         'Подтвердите регистрацию!',
    #         (
    #             f"Благодарим за регистрацию на сайте V-magazine.\n"
    #             "Для активации учётной записи, пожалуйста перейдите по ссылке:\n"
    #             f"http://localhost:8000/{activation_url}\n"
    #         ),
    #         settings.EMAIL_HOST_USER,
    #         [user.email],
    #         fail_silently=False,
    #     )
    #     return redirect('email_confirmation_sent')


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
