from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate, login
from .models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm

from django.views.decorators.http import require_http_methods
from .forms import ServiceRequestForm
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('account_info')
    else:
        form = AuthenticationForm()
    return render(request, 'customer_service/login.html', {'form': form})
def homepage(request):
    return render(request, 'customer_service/homepage.html')

@require_http_methods(["POST", "GET"])
def custom_logout(request):
    logout(request)
    return redirect('login')
@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.user = request.user
            request_obj.save()
            return redirect(reverse('track_requests'))
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    user_requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'customer_service/track_requests.html', {'requests': user_requests})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the new user
            return redirect('account_info')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def account_info(request):

    user_requests = ServiceRequest.objects.filter(user=request.user).order_by('-created_at')[:5]
    return render(request, 'customer_service/account_info.html', {'requests': user_requests})
