from django.shortcuts import render,redirect
from api.enums import Commune 
from api.models import Parking,Verificateur
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    parkings = Parking.objects.all()
    
    return render(request , 'home.html', {'parkings':parkings})

def add_parking(request):
    # Get the choices from the Commune enum directly
    commune_choices = [c.name for c in Commune]
    
    # Pass the choices to the template context
    context = {
        'commune_choices': commune_choices
    }
    if request.method == "POST":
        name = request.POST.get('name')
        localisation = request.POST.get('local')
        commune = request.POST.get('commune')
        capacite = request.POST.get('capacite')
        
        parking = Parking.objects.create(
            name=name,
            localisation=localisation,
            commune=commune,
            capacite=capacite
        )
        parking.save()
        
        return redirect('home')
    
    return render(request, 'add_parking.html', context)

# @api_view(['POST'])
# def add_verificateur(request):
#     if request.method == "POST":
#         parkings = Parking.objects.all()
#         if request.method == "POST":
#             first_name = request.data.get('first_name')
#             last_name = request.data.get('last_name')
#             email = request.data.get('email')
#             password = request.data.get('password')
#             parking = request.data.get('parking')
#             parking = Parking.objects.get(id=parking)
            
#             verificateur = Verificateur.create_user(first_name=first_name,
#                                                 last_name=last_name,
#                                                 email=email,
#                                                 password=password,
#                                                 parking=parking)
#             verificateur.save()
            
#             return redirect('home')
#     return render(request, 'add_verificateur.html', {'parkings':parkings})
            