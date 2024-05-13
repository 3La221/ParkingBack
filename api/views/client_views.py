from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from ..serializers import ClientSerializer,VoitureSerializer,ParkSerializer
from rest_framework.permissions import IsAuthenticated
from ..models import Client


@api_view(['POST'])
def register(request):
    if request.method == "POST":
        serializer = ClientSerializer(data=request.data, many=False)

        if serializer.is_valid():
            user = serializer.save()
            tokens = RefreshToken.for_user(user)
            return Response({
                'id':user.id ,
                'refresh': str(tokens),
                'access' : str(tokens.access_token)
            },status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method == "POST":
        user = authenticate(email=request.data.get("email"),
                            password=request.data.get("password"))
        if user:
            tokens = RefreshToken.for_user(user)
            return Response({
                'id':user.id ,
                'refresh': str(tokens),
                'access' : str(tokens.access_token)
            },status=status.HTTP_200_OK)
            
        else:
            return Response({'detail': 'Invalid credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)
            
            
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ajouter_voiture(request):
    if request.method == "POST":
        client = Client.objects.get(id=request.user.id)
        try:
            id = request.data.pop("id")
        except:
            id = None
        if id:
            client.voiture.add(id)
            return Response({
                f'Voiture {id} ajoute au {client}'},
                status=status.HTTP_200_OK
            )
        serializer = VoitureSerializer(data=request.data,many=False)
        if serializer.is_valid():
            voiture = serializer.save()
            client.voiture.add(voiture)
            return Response({
                    'message': 'Voiture ajoutée au client avec succès',
                    'voiture': serializer.data,
                }, status=status.HTTP_201_CREATED  )
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def stationer(request):
    if request.method == "POST":
        request.data["client"] = request.user
        serializer = ParkSerializer(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    