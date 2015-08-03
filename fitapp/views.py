from django.shortcuts import render, render_to_response


def fitHome(request):
    return render_to_response('fithome.html')


def dashboard(request):
    return render_to_response('dashboard.html')


def impress(request):
    return render_to_response('impress.html')


def liveworkout(request):
    return render_to_response('liveworkout.html')


def login(request):
    return render_to_response('login.html')

def logout(request):
    return render_to_response('logout.html')

def news(request):
    return render_to_response('news.html')


def register(request):
    return render_to_response('register.html')


def videoworkout(request):
    return render_to_response('videoworkout.html')


def team(request):
    return render_to_response('team.html')


def blog(request):
    return render_to_response('blog.html')


def dashboard(request):
    return render_to_response('dashboard.html')


def contact(request):
    return render_to_response('contact.html')


def men(request):
    return render_to_response('men.html')


def women(request):
    return render_to_response('women.html')


def company(request):
    return render_to_response('company.html')


def coaching(request):
    return render_to_response('coaching.html')


def programm(request):
    return render_to_response('programm.html')


def seminar(request):
    return render_to_response('seminar.html')


def anamnese(request):
    return render_to_response('anamnese.html')


def pricing(request):
    return render_to_response('pricing.html')


def agb(request):
    return render_to_response('agb.html')
