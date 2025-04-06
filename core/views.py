from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request,'core/accueil.html')

def propos(request):
    return render(request,'core/propos.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm  # Vérifie que ton formulaire est bien importé

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm  # Vérifie que ton formulaire est bien importé
from django.db.models import Q  # Pour permettre la recherche par username OU email
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_blog(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']  # Peut être un username ou un email
            password = form.cleaned_data['password']

            # Chercher l'utilisateur par username ou email
            user = User.objects.filter(Q(username=identifier) | Q(email=identifier)).first()

            if user is not None:
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "✅ Connexion réussie. Bienvenue !")
                    return redirect('accueil')

            messages.error(request, "❌ Nom d'utilisateur, e-mail ou mot de passe incorrect.")
        else:
            messages.error(request, "❌ Erreur dans le formulaire. Vérifiez vos informations.")
    else:
        form = LoginForm()

    return render(request, "core/login.html", {"form": form})



from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Compte créé avec succès ! Connectez-vous.")
            return redirect('login_blog')
    else:
        form = RegisterForm()

    return render(request, "core/register.html", {"form": form})

def logout_blog(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('login_blog')





