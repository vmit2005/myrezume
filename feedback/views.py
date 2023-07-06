from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FeedbackForm
from .models import Feedback
from django.core.paginator import Paginator

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from telebot.models import Telesettings
from sendmessage import send_telegram
from re import findall





def feedbacks(request):
    feeds = Feedback.objects.order_by('id')
    p = Paginator(feeds, 4)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    return render(request, 'feedback/feedback.html', {'page_obj': page_obj})


# def detail(request, feed_id):
#     return render(request, 'feedback/details.html', {'id': feed_id})
#

# def new_feedback(request):
#     return render(request, 'feedback/newfeedback.html')

@login_required
def new_feedback2(request):
    global user
    user = request.user

    print('USR', user)
    if request.user.is_authenticated:

        print(request.user)
        if request.method == 'POST':
            form = FeedbackForm(request.POST)

            if form.is_valid():
                form.save()
                print(form.data, type(form))
                # ff = form_sort(form)
                send_telegram(tg_title=form.data['title'], tg_author=form.data['author'],tg_mail=form.data['mail'],tg_description=form.data['description'])
                return redirect('feedback')
            else:

                error: "Данные неверны"

        form = FeedbackForm(initial={'value': 'bbb'})
        data = {
            'form': form,
            # 'error': error
        }
    return render(request, 'feedback/newfeedback2.html', data)


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'feedback/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('feedback')
            except IntegrityError:
                return render(request, 'feedback/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'Такое имя пользователя уже существует. Задайте другое или войдите'
                })
        else:
            return render(request, 'feedback/signupuser.html', {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают'
            })


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'feedback/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'feedback/loginuser.html', {
                'form': AuthenticationForm(),
                # 'error': 'Неверные данные для входа'
            })
        else:
            login(request, user)
            return redirect('newfeedback2')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def currenttodos(request):
    # todos = Todo.objects.all()
    todos = Todo.objects.filter(user=request.user,
                                date_completed__isnull=True)
    return render(request, 'feedback/currenttodos.html', {'todos': todos})
