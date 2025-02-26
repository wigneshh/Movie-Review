from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import Movie
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import logout

def your_api_view(request):
    return JsonResponse({'message': 'API is working'})

def logout_view(request):
    logout(request)  # Logs the user out
    return redirect('login')  # Redirect to homepage (change if needed)


@csrf_exempt
def my_view(request):
    return JsonResponse({'message': 'CSRF disabled for debugging'})
    return render(request, 'login.html')

def index(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})

def reviews(request):
    movies = Movie.objects.all()
    return render(request, 'pages/reviews.html', {'movies': movies})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Login attempt: Username={username}, Password={password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(f"Authentication successful! Logged in as: {user.username}")
            auth_login(request, user)
            return redirect('index')
        else:
            print("Authentication failed: Invalid credentials")
            return render(request, 'pages/login.html', {'error': 'Invalid username or password'})

    return render(request, 'pages/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'pages/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'pages/register.html', {'error': 'Username already exists'})

        if User.objects.filter(email=email).exists():
            return render(request, 'pages/register.html', {'error': 'Email already registered'})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        auth_login(request, user)
        return redirect('index')  

    return render(request, 'pages/register.html')

def add_review(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        rating = request.POST.get('rating')
        review = request.POST.get('reviewText')

        Movie.objects.create(title=title, genre=genre, rating=rating, review=review)
        return redirect('reviews')

    return render(request, 'pages/reviews.html')  