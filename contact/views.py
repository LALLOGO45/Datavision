from django.shortcuts import render

# Create your views here.
# contact/views.py
from django.shortcuts import render,redirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Traiter le message (par exemple, envoyer un email)
            return render(request, 'contact/merci.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


#
# Vue pour la page de remerciement
def merci(request):
    return render(request, 'contact/merci.html')


from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render
from .models import Message

@csrf_exempt
def send_email(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Enregistrer le message dans la base de données
        try:
            new_message = Message.objects.create(
                nom=nom,
                email=email,
                message=message
            )
            new_message.save()

            to_email = "cabdatavision@gmail.com"
            cc_email = "lassanelallogo2002@gmail.com"

            subject = f"Nouveau message de {nom}"
            body = f"Nom: {nom}\nEmail: {email}\n\nMessage:\n{message}"

            # Envoyer l'email
            email_message = EmailMessage(
                subject=subject,
                body=body,
                from_email=email,
                to=[to_email],
                cc=[cc_email]
            )
            email_message.send(fail_silently=False)

            return render(request, 'contact/merci.html')
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Méthode non autorisée"}, status=405)
