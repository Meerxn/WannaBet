from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from WannaBet.models import Event
from WannaBet.models import Bet
# Create your views here.

def index(request):
    return render(request, 'WannaBet/index.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect(reverse('login'))

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 
        # Fetch the username from the user db
        user = User.objects.filter(username=username)
        # if there is a user we authenticate it or say oh no there isnt one 
        if user.count()>=1:
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return redirect(reverse('home'))
            return render(request, 'WannaBet/login.html', context={'alert':'warning','alert_msg':'Username or Password did not match'})
    return render(request,'WannaBet/login.html', context={"title":"login"})

def register(request):
    if request.method == "POST":        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password') 
        verify = request.POST.get('verify')

        if password == verify:
            if User.objects.filter(email=email).count() != 0:
                return render(request, 'WannaBet/register.html', context={'alert':'warning','alert_msg':'An account has already been registered with this Email address!'})
            if User.objects.filter(username=username).count() != 0:
                return render(request, 'WannaBeton/register.html', context={'alert':'warning','alert_msg':'An account has already been registered with this Username!'})
            user = User.objects.create_user(username=username, email= email, password = password)
            return(render(request,'WannaBet/home.html'))

    return render(request,'WannaBet/register.html')

@login_required
def home(request):
    return render(request,'WannaBet/home.html')
 

# This is for events
@login_required
def create_event(request):
    if request.method == "POST":
        event_name = request.POST.get("event_name")
        # time = re....
        if all([event_name]):
            event, created = Event.objects.get_or_create(name = event_name)
            if created:
                event.save()
            return redirect(reverse('home'))
    return render(request,'WannaBet/create_event.html')
 

#This method is responsible for joining a bet using a code from generate code 

def create_bet(request):   
 if request.method == "POST":
    bet_name = request.POST.get("bet_name")
     
    if all([bet_name]):
     bet, created = Bet.objects.get_or_create(name = bet_name)
     if created:
        bet.save()
     return redirect(reverse('home'))
 return render(request,'WannaBet/create_bet.html')
     


#This method is responsible for creating the code for joining a bet or creating a bet 
def createCode(request):  
    return  

#follow another user method need to know how to import another user (graph algo model maybe needed )
def follow(request): 
    return 


