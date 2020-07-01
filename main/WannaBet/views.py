from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'WannaBet/index.html')

def login(request):
    return render(request, 'WannaBet/login.html')
  

# Create your views here.

# This method is responsible  for creating a bet 
# Need to know how to push a new bet to the back end 
def createBet(request,code):
    return



#This method is responsible for joining a bet using a code from generate code 
def joinBet(request,code):   
    return 


#This method is responsible for creating the code for joining a bet or creating a bet 
def createCode(request):  
    return  

#follow another user method need to know how to import another user (graph algo model maybe needed )
def follow(request): 
    return 



# def login (request)
# dont know if this needs a method     


