from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student, Course, Lecturer, CustomUser
from .forms import CustomUserCreationForm


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember')  # Handling remember me functionality

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Handle "Remember me" functionality
            if remember_me:
                request.session.set_expiry(3600*24*7)  # Session will last for a week if "Remember me" is checked
            else:
                request.session.set_expiry(0)  # Session expires when the browser is closed

            # Redirecting to the appropriate dashboard based on user type
            if user.user_type == 'student':
                return redirect('student_dashboard')
            elif user.user_type == 'lecturer':
                return redirect('lecturer_dashboard')
            else:
                logout(request)  # Invalid user type, so log the user out
                return render(request, 'error.html', {'message': 'Invalid user type.'})
        else:
            messages.error(request, 'Invalid username or password')  # Use messages framework for errors
            return render(request, 'login.html')

    return render(request, 'login.html')


# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')


# Student Dashboard View
def student_dashboard(request):
    student = request.user.student  # Corrected related_name
    context = {
        'student': student,
    }
    return render(request, 'student_dashboard.html', context)

# Lecturer Dashboard View
def lecturer_dashboard(request):
    lecturer = request.user.lecturer  # Corrected related_name
    courses = request.user.courses.all()
    context = {
        'lecturer': lecturer,
        'courses' : courses
    }
    return render(request, 'lecturer_dashboard.html', context)

#Signup view
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            user = form.save(commit=False)
            user_type = request.POST.get('user_type')
            if user_type in ['student', 'lecturer']:
                user.user_type = user_type
            else:
                user.user_type = 'student'
            user.save()

            # If the user is a student, create a student profile with the profile picture
            if user.user_type == 'student':
                Student.objects.create(user=user, profile_picture=form.cleaned_data.get('profile_picture'))

            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
