from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    template_name = 'login.html'
    # Redirigir si el usuario ya está autenticado
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página que desees tras el login
        else:
            messages.error(request, 'Email o contraseña incorrectos.')
    
    return render(request, template_name)  # Nombre de tu template

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')

        if password == password_repeat:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Este correo electrónico ya está registrado.')
            else:
                user = User.objects.create_user(
                    username=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.success(request, 'Tu cuenta ha sido creada exitosamente.')
                return redirect('login')  # Redirige al login después del registro
        else:
            messages.error(request, 'Las contraseñas no coinciden.')
    
    return render(request, 'register.html')  # Nombre de tu template de registro

def logout_view(request):
    logout(request)
    return redirect('login')