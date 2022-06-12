from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from core.models import NewUserTB
from django.core.mail import EmailMultiAlternatives,BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.

def signup(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pwd = request.POST.get('password')
        NewUserTB(name=nm,email=em,password=pwd).save()
        if nm and em:
            subject = 'regarding testing!'
            message = render_to_string('render_template.html')
            text_content = strip_tags(message)
            email_from = settings.EMAIL_HOST_USER
            recipient = [em]
            try:
                email = EmailMultiAlternatives(subject,text_content,email_from,recipient)
                email.attach_alternative(message,'text/html')
                email.send()
                return HttpResponse(f'hello {nm} you have successfully registered!!')
            except BadHeaderError:
                return HttpResponse(f'hello {nm} there is some problem please check')
    return render(request, 'signup.html')
