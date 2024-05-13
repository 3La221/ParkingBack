from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import ClientManager
from .utils import generate_short_id
import uuid
import qrcode 
from .enums import Commune
from django.utils import timezone



# Create your models here.

class Parking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)    
    localisation = models.URLField(max_length=200, null=True, blank=True)
    commune = models.CharField(max_length=100, choices=[(c.name, c.value) for c in Commune])
    capacite = models.IntegerField(default=10, null=True, blank=True)

    def __str__(self) -> str:
        return f'Parking {self.name}'

    def save(self, *args, **kwargs):
        data = f"{self.name},{self.commune},{self.capacite} , ID = {self.id}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = f"static/qrs/parking_qr_{self.id}.png"  # Adjust the path as needed
        
        img.save(img_path)
        
        self.qr_code_path = img_path
        
        super().save(*args, **kwargs)



class Profile(AbstractUser):
    username = None
    numero_tel = models.CharField(max_length=12 , null=True , blank=True)
    email = models.EmailField(unique=True)
    PASSWORD_FIELD = 'password'
    objects = ClientManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['numero_tel']
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}' 
    


class Verificateur(Profile):
    verif_id = models.CharField(primary_key=True, default=generate_short_id, editable=False, max_length=8)
    parking = models.ManyToManyField(Parking,related_name="verifcateurs")
    
    
    def __str__(self) -> str:
        return f'Verif/{self.first_name} {self.last_name}'


class Client(Profile):
    voiture = models.ManyToManyField("Voiture",related_name="owners",blank=True)
    


    


class Voiture(models.Model):
    id = models.CharField(primary_key=True,
                        default=generate_short_id,
                        editable=False,
                        max_length=8)
    matricule = models.CharField(max_length=15, unique=True)
    numero_type = models.CharField(max_length=15, unique=True, null=False)
    marque = models.CharField(max_length=30,null=True,blank=True)
    model = models.CharField(max_length=30,null=True)
    
    
    def __str__(self) -> str:
        return self.matricule


class Park(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dateDebut = models.DateTimeField(default=timezone.now) 
    dateFin = models.DateTimeField(null=True , blank=True)
    parking = models.ForeignKey(Parking,on_delete=models.CASCADE, related_name="parks",null=True) 
    voiture = models.ForeignKey(Voiture,on_delete=models.CASCADE, related_name="parks",null=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE, related_name="parks",null=True)
    cout = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    
        
    def __str__(self) -> str:
        return f'{self.voiture} {self.parking} {self.dateDebut}'
    

    
    
    