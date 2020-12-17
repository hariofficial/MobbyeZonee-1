from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        mailid = request.POST['mailid']
        password = request.POST['password']

        user = User.objects.create_user(
            username=name, number=number, email=mailid, password=password)
        user.save()
        return redirect('/')

    else:
        return render(request, 'signup.html')


def home(request):
    return render(request, 'home.html')


def cart(request):
    return render(request, 'cart.html')
