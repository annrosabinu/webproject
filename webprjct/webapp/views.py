from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Home page view
def home(request):
    return render(request, 'home.html')

# Login page view
def loginpage(request):
    return render(request, 'login.html')

# Signup page view
def signup(request):
    return render(request, 'signup.html')

# About page view
def about(request):
    return render(request, 'about.html')

# User registration functionality view
def usercreate(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']

        if password == cpassword:  # Password matching
            if User.objects.filter(username=username).exists():  # Check if username already exists
                messages.info(request, 'This username already exists!')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email
                )
                user.save()
                messages.success(request, "Account created successfully!")
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')

        return redirect('loginpage')

    return render(request, 'signup.html')


def user_login(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('adminhome')
            else:
                 auth.login(request, user) 
                 messages.success(request, f'Welcome, {username}!')
            return redirect('about')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('loginpage')

    return render(request, 'login.html')

# User logout functionality view
def logout_view(request):
    auth.logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('home')

def adminhome(request):
    return render(request,'admin.html')