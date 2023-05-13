from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .utils import DataMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .models import Student
from .forms import *
from .models import *


def main(request):  # главная страница
    return render(request, "main.html")


def register(request):  # страница регистрации
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            student = Student.objects.create(
                phone_number="Введите контактный телефон", organization="Введите учреждение", about="",
                user=form.save(), image="zoro.jpg"
            )  # создание профиля для пользователя
            messages.success(request, f'Вы успешно зарегистрировались. Теперь вы можете войти.')
            return HttpResponseRedirect("log_in")  # перевод на страницу входа
        else:
            messages.success(request, f'Ошибка! Проверьте корректность введенных данных')  # сообщение об ошибке
    form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, "registration.html", context)


def article_delete(request):
    return render(request, "")


def article_edit(request):
    return render(request, "")


def download_article(request):
    return render(request, "")


def article(request, pk):  # страница информации о статье
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, "article.html", context)


def article_add(request):
    return render(request, "")


@login_required
def articles(request):
    article = Article.objects.filter(user=request.user)
    context = {
        'articles': article,
    }
    return render(request, "select_article.html", context)


def event_delete(request):
    return render(request, "")


def event_edit(request):
    return render(request, "")


def event(request, pk):  # страница информации о конференции
    event = get_object_or_404(Event, pk=pk)
    orgs = User.objects.filter(
        event_user__event_id_id=pk,
        event_user__is_org="True"
    )
    context = {
        'event': event,
        'orgs': orgs
    }
    return render(request, "conference.html", context)


def add_event(request):
    return render(request, "")


def events(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, "select_conference.html", context)


def my_events(request):
    events = Event.objects.filter(user=request.user)
    context = {
        'events': events
    }
    return render(request, "select_conference.html", context)


def profile_edit(request):
    return render(request, "")


def event_speakers(request):
    return render(request, "select_profile.html")


@login_required
def profile(request):  # страница профиля
    stud = Student.objects.get(user=request.user)
    if stud.phone_number == "Введите телефон":  # перевод на страницу редактирования профиля
        return HttpResponseRedirect("edit_profile")
    return render(request, "profile.html")


class LoginUser(DataMixin, LoginView):  # класс для авторизации пользователя
    form_class = LoginForm
    template_name = 'log_in.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Вход")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('profile')
