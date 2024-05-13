from datetime import datetime, timedelta
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.utils import timezone
from .models import *


class VoitureSerializer(ModelSerializer):
    class Meta:
        model = Voiture
        fields = ['id','matricule','marque','model','numero_type','owners']
        read_only_fields = ['id','owners']
        
        
class ClientSerializer(ModelSerializer):
    voiture = VoitureSerializer()
    class Meta:
        model = Client
        fields = '__all__'
        
    def create(self,validated_data):
        voiture_data = validated_data.pop("voiture")
        
        voiture = Voiture.objects.create(**voiture_data)
        user = Client.objects.create_user(**validated_data)
        user.voiture.add(voiture)
        return user 



    
class VerificateurSerializer(ModelSerializer):
    class Meta:
        model = Verificateur
        fields = "__all__"
        exclude = ('profile_ptr', )

        
    def create(self,validated_data):
        parkings = validated_data.pop("parking")
        
        user = Verificateur.objects.create_user(**validated_data)
        
        for parking in parkings:
            user.parking.add(parking)

        return user
    



class ParkingSerializer(ModelSerializer):
    class Meta:
        model = Parking
        fields = '__all__'

class ParkSerializer(ModelSerializer):
    class Meta:
        model = Park
        fields = '__all__'
    
    
    def to_representation(self, instance):
        
        
        data = super().to_representation(instance)
        data["client"] = f'{instance.client.first_name} {instance.client.last_name}'
        
        data["dateDebut"] = instance.dateDebut.strftime("%Y-%m-%d %H:%M:%S")
        try:
            data["dateFin"] = instance.dateFin.strftime("%Y-%m-%d %H:%M:%S")
        except:
            data["dateFin"] = None
        return data
    
    
    
    def create(self, validated_data):
        print(validated_data)
        park , created = Park.objects.get_or_create(**validated_data,done=False)
        if  created :
            return park
        
        park.dateFin = timezone.now()
        duration = park.dateFin - park.dateDebut
        two_hours = timedelta(hours=2)
        t = duration - two_hours #hadi ch7al 93ad w9t fo9 2h
        park.cout = 50
            
        while t > timedelta(minutes=0):
            park.cout += 20
            t -= timedelta(hours=1) 
        park.done = True
        park.save()
        return park 
            
            

