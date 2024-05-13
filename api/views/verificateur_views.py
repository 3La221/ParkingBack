
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import Parking,Voiture,Park
from ..serializers import VerificateurSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsVerificateur




        

@api_view(['POST'])
def login_verificateur(request):
    if request.method == "POST":
        user = authenticate(email=request.data.get("email"),
                            password=request.data.get("password"))
        if user:
            tokens = RefreshToken.for_user(user)
            return Response({
                'id':user.verificateur.verif_id ,
                'refresh': str(tokens),
                'access' : str(tokens.access_token)
            },status=status.HTTP_200_OK)
            
        else:
            return Response({'detail': 'Invalid credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)
            
            
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsVerificateur])
def verif_voiture(request, id):
    parking = Parking.objects.get(id=id)
    voiture = Voiture.objects.get(id=request.data.get('voiture'))
    try:
        Park.objects.get(
        parking=parking,
        voiture=voiture,
        done=False
        )
        return Response({'parked':True,'detail': 'This car is already Parked'},status==status.HTTP_200_OK)
    except Park.DoesNotExist:
        return Response({'parkde':False,'detail': 'This car is not  Parked'},
                        status=status.HTTP_200_OK)
    
        
                
        
        
    