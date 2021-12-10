from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def home(request):
    return render(request, 'main/home.html')
    
def about(request):
    return render(request, 'main/about.html')

def videos(request):
    return render(request, 'main/videos.html')

def services(request):
    return render(request, 'main/services.html')

def blog(request):
    return render(request, 'main/blog.html')

def contact(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        body = 'Name: ' + name + '\n' + 'Email: ' + email + '\n' + 'Phone: ' + phone + '\n' + 'Subject: ' + subject + '\n' + 'Message: ' + message

        send_mail('New Contact Form Submission.',
         body,
         settings.EMAIL_HOST_USER,
         ['shridhar.patel@live.com'],
         fail_silently=False)

    return render(request, 'main/contact.html')