from ..serializers import ParkSerializer,VoitureSerializer,ParkingSerializer
from rest_framework import generics
from ..models import Voiture,Parking,Park
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers import VerificateurSerializer




class VoitureListAPIView(generics.ListAPIView):
    serializer_class = VoitureSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Voiture.objects.filter(owners__id=user_id)
        return Voiture.objects.all()


class ParkingListAPIView(generics.ListAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer


class ParkListPIView(generics.ListAPIView):
    serializer_class = ParkSerializer
    
    def get_queryset(self):
        queryset = Park.objects.all()
        
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(client__id=user_id)
            
        parking_id = self.request.query_params.get('parking_id')
        if parking_id:
            queryset = queryset.filter(parking__id=parking_id)
            
        car_id = self.request.query_params.get('car_id')
        if car_id:
            queryset= queryset.filter(voiture__id=car_id)
        
        return queryset


class ParkRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Park.objects.all()
    serializer_class = ParkSerializer
    

@api_view(['POST'])
def add_verificateur(request):
    if request.method == "POST":
        serializer = VerificateurSerializer(data=request.data,many=False)
        if serializer.is_valid():
            user = serializer.save()
            print("Serializer",serializer)
            return Response({"Verificateur Added !!"},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
