from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('create_event/', views.create_event, name='create_event'),
    path('create_bet/',views.create_bet, name = 'create_bet'),
    path('bet/<uuid:bet_code>', views.bet_page, name='bet'),
     path('join_bet/<uuid:bet_code>', views.join_bet, name='join_bet')
]