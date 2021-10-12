from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.hashers import make_password
import random
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is None:
            messages.info(request,'Invalid Credentials')
            return redirect('/')

        else:
            auth.login(request,user)
            messages.info(request,'Login Success')
            return redirect('/')

def logout(request):
    auth.logout(request)
    messages.info(request,'logout successfull')
    return redirect('/')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_nmae']
        username = request.POST['username']
        password = request.POST['password']
        print(username,User.objects.filter(username=username))
        if User.objects.filter(username=username).exists():
            messages.info(request,'You are already registered')
            return redirect('/')
        else:
            otp = random.randint(000000,999999)
            request.session['otp']=otp
            link = f'aniketvyas4.pythonanywhere.com/accounts/verifyEmail/f{otp}'
            email = EmailMessage('Verification Mail',f'Hey, {first_name}, Please use the following link '+link+' for your verification',settings.EMAIL_HOST_USER,[username])
            email.fail_silently=False
            email.send()
            intermediateVerficationModal(
                username=username,
                last_name =last_name,
                first_name=first_name,
                password=password,
                verficationStatus = False,
                otp=otp
                ).save()
            request.session['first_name'] = first_name
            request.session['last_name'] = last_name
            request.session['username'] = username
            request.session['password'] = password
            print(request.session)
            messages.info(request,'Please Check your Email and do as directed!')
            return redirect('/')

def verifyEmail(request,id):
    print(request.session)
    if intermediateVerficationModal.objects.filter(otp=otp).exists():
        User.objects.create_user(
            first_name=request.session['first_name'],
            last_name = request.session['last_name'],
            username = request.session['username'],
            password = request.session['password']
        )
        user = auth.authenticate(username=request.session['username'],password=request.session['password'])
        auth.login(request,user)
        messages.info(request,'verification completed amd you are logged in!')
        return redirect('/')
    else:
        email = EmailMessage('Error occured at website',f'Hey, {first_name}, Error occured at verifyEmail',settings.EMAIL_HOST_USER,[username])
        email.fail_silently=False
        email.send()
        messages.info(request,'Error Occured, Try again later!')
        return redirect('/')
