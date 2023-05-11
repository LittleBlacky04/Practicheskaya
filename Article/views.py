from django.shortcuts import render
from .models import Event
from .models import Article

from .forms import LoginUser
from .forms import Registration

def main(request):
    # теги блока welcome-banner
    welcome_h2 = "Возможности"
    welcome_about = "Мероприятия, статьи.  Помогаем работать, учиться и находить единомышленников в любом городе."
    # теги блока 3-last-conference
    conference_h2 = "Последние мероприятие"
    conference_a = "все мероприятия"
    events = Event.objects.all()[:3] # Нужно ограничить до 3 элементов
    # теги блока 3-last-article
    article_h2 = "Последние статьи"
    article_a = "все статьи"
    articles = Article.objects.all()[:3] # Нужно ограничить до 3 элементов
    data={"welcome_h2":welcome_h2, "welcome_about":welcome_about,
          "conference_h2":conference_h2, "conference_a":conference_a, "events":events,
          "article_h2":article_h2, "article_a":article_a, "articles":articles}
    return render(request, "main.html", context=data)

def conference(request):
    # теги блока view
    events = Event.objects.all()
    data={"events":events}
    return render(request, "conference.html", context=data)

def article(request):
    # теги блока view
    articles = Article.objects.all() 
    data={"articles":articles}
    return render(request, "article.html", context=data)

def select_conference(request):
    event = Event.objects.all()[:1]
    orgs = ''
    data={"event":event, 'orgs':orgs}
    return render(request, "select_conference.html", context=data)

def select_article(request):
    article = Article.objects.all()[:1]
    author = ''
    data = {"article": article, "author": author}
    return render(request, "select_article.html", context=data)

def profile(request):
    data={}
    render(request, "profile.html", context=data)

def select_profile(request):
    user = ''
    # теги блока 3-last-conference
    conference_h2 = "Последние мероприятие"
    conference_a = "все мероприятия"
    events = Event.objects.all()[:3]  # Нужно ограничить до 3 элементов
    # теги блока 3-last-article
    article_h2 = "Последние статьи"
    article_a = "все статьи"
    articles = Article.objects.all()[:3]  # Нужно ограничить до 3 элементов
    data = {"user": user,
            "conference_h2": conference_h2, "conference_a": conference_a, "events": events,
            "article_h2": article_h2, "article_a": article_a, "articles": articles}
    render(request, "select_profile.html", context=data)

def log_in(request):
    login_form = LoginUser()
    data = {"form": login_form}
    render(request, "profile.html", context=data)

def register(request):
    register_form = Registration()
    data = {"form": register_form}
    render(request, "profile.html", context=data)