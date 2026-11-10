from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout

# Create your views here.
def index(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
            form = UserCreationForm()   
    return render(request, 'index.html', {'form': form})    

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
def logout(request):
    auth_logout(request)
    return redirect('login')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')

def book_appointment(request):
    return render(request, 'book_appointment.html')
