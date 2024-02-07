from django.shortcuts import render, redirect
from .models import Llamada
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    # Obtener todas las llamadas asociadas al usuario autenticado
    llamadas = Llamada.objects.filter(user=request.user)
    data = {
        'llamadas': llamadas
    }
    # Renderizar la página de inicio con la lista de llamadas del usuario
    return render(request, 'home.html', data)


def registro(request):
    # Inicializar el formulario de registro de usuario
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        # Procesar el formulario de registro cuando se envía
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            # Guardar el nuevo usuario y autenticarlo
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            # Redirigir al usuario a la página de inicio después del registro exitoso
            return redirect(to="home")
        data["form"] = formulario
    # Renderizar la página de registro con el formulario correspondiente
    return render(request, 'registration/registro.html', data)


def calcular_pago(request):
    # Obtener todas las llamadas (posiblemente para calcular algún pago)
    data = Llamada.objects.all()
    # Renderizar la página de boleta con los datos de todas las llamadas
    return render(request, 'boleta.html', {'llamadas': data})