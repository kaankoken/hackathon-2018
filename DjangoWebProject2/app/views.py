"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Ana Sayfa',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Iletisim',

            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Hakkimizda',
            'year':datetime.now().year,
        }
    )

def registration(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'title':'Kayit',
            'year':datetime.now().year,
        }
    )

def user_registration(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('E-posta adresi')
            raw_password = form.cleaned_data.get('Parola')
            user = authenticate(username = username, password = raw_password, tur = "kullanici")
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'app/user_registration.html', {'form': form})

def inst_registration(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('E-posta adresi')
            raw_password = form.cleaned_data.get('Parola')
            tanim = form.cleaned_data.get('Aciklama')
            user = authenticate(username = username, password = raw_password, tur = "kurum")
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'app/user_registration.html', {'form': form})

def log_user(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/user.html',
        {
            'title' : 'User',
            'year': datetime.now().year,
            }
        )

def log_inst(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/inst.html',
        {
            'title' : 'Institution',
            'year': datetime.now().year,
            }
        )

def institution_main(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/institution_main.html',
        {
            'title' : 'Ana Sayfam(Kurum)',
            'year': datetime.now().year,
            }
        )

def client_main(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/client_main.html',
        {
            'title' : 'Kullanici Ana Sayfasi',
            'year': datetime.now().year,
            }
        )
def my_reservation(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/my_reservation.html',
        {
            'title' : 'Seans Bilgisi',
            'year': datetime.now().year,
            }
        )

def my_modules(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/my_modules.html',
        {
            'title' : 'Modullerim',
            'year': datetime.now().year,
            }
        )

def my_labs(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/my_labs.html',
        {
            'title' : 'Laboratuvarlarim',
            'year': datetime.now().year,
            }
        )