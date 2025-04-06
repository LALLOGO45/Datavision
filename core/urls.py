# core/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('propos/',views.propos,name='propos'),
    path('login/',views.login_blog,name='login_blog'),
    path('register/',views.register,name='register'),
    path('logout/', views.logout_blog, name='logout_blog'),
    # Page pour demander la réinitialisation du mot de passe
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    # Message de confirmation après l'envoi de l'email
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # Lien dans l'email pour entrer un nouveau mot de passe
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # Confirmation que le mot de passe a été changé
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

