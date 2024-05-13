
from django.contrib import admin
from django.urls import path

from .views import client_views,admin_views,verificateur_views

from rest_framework_simplejwt.views import TokenRefreshView

refresh_jwt_token = TokenRefreshView.as_view()

urlpatterns = [
    #Authentication
    path('register/',client_views.register,name="register-client"),
    path('login/',client_views.login,name="login-client"),
    path('token/refresh/', refresh_jwt_token, name='token_refresh'),
    
    #Client Endpioints
    path('add_car/',client_views.ajouter_voiture,name="add-car"),
    path('park_in_out/',client_views.stationer,name="park-in"),
    
    
    #Admin Endpoints
    path('cars/', admin_views.VoitureListAPIView.as_view(), name='voiture-list'),
    path('parkings/', admin_views.ParkingListAPIView.as_view(), name='parking-list'),
    path('parks/',admin_views.ParkListPIView.as_view() , name="parks-list"),
    path('add_verificateur/',admin_views.add_verificateur,name="add-verificateur"),
    
    
    #Verificateur Endpoints
    path('login_verificateur/',verificateur_views.login_verificateur,name="login-verificateur"),
    path('check_park/<str:id>/',verificateur_views.verif_voiture,name="check-park")
    
]
