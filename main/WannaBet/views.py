from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from WannaBet.models import Event, Bet, Profile, Relationship
from django.http import HttpResponseNotFound

# Create your views here.

def index(request):
    return render(request, 'WannaBet/index.html')

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
                return render(request, 'WannaBet/register.html', context={'alert':'warning','alert_msg':'An account has already been registered with this Username!'})

            user = User.objects.create_user(username=username, email= email, password = password)
            profile, create = Profile.objects.get_or_create(user = user)
            if create:
                profile.save()
            return(render(request,'WannaBet/home.html'))

    return render(request,'WannaBet/register.html')

@login_required
def home(request):
    choices_for_sides = {'W':'Win', "L":"Lose", "D":"Draw"}

            
    events = Event.objects.all()
    profile = Profile.objects.filter(user = request.user).get()
    bets = Bet.objects.filter(members = request.user)
    # sides = Sides.objects.filter(bet = bets)
    # betters_profiles = [Profile.objects.filter(x.members).get() for x in bets]
    context = {"bets":[x for x in bets]}
    return render(request,'WannaBet/home.html', context=context)
 

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
@login_required
def create_bet(request):   
    events = Event.objects.all()
    context = {"events":[x for x in events]}
    # Add Authenticated models
    if request.user.is_authenticated:
        if request.method == "POST":
            event_name = request.POST.get("event_name")
            bet_name = request.POST.get("bet_name")
            
            if all([bet_name, event_name]):
                profile = Profile.objects.filter(user = request.user)
                event = Event.objects.filter(name = "Trial")[0]
                bet, created = Bet.objects.get_or_create(event= event)
                # sides, recreated = Sides.objects.get_or_create(profile = profile)
                # if recreated:
                #     sides.bet =  bet
                #     sides.side = 'Win'
                #     side.save()
                if created:
                    bet.name = bet_name
                    bet.members = profile
                    bet.save()
                return redirect(reverse('home'))
    return render(request,'WannaBet/create_bet.html', context=context)
        

def bet_page(request, bet_code):
    bet = Bet.objects.filter(identifier = str(bet_code))
    if bet.count()>0:
        bet = bet.get()
    else:
        return HttpResponseNotFound("<h1>Page Not Found</h1>")
    context = {"bet":bet}
    return render(request, 'WannaBet/bet.html', context=context)

#follow another user method need to know how to import another user (graph algo model maybe needed )
def follow(request): 
    return 


