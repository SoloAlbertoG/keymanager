from django.db import models
from django.dispatch import receiver
from Crypto.PublicKey import RSA
from django.http import HttpResponse, HttpRequest
from django.http import FileResponse
# Create your models here.
class Registro(models.Model):
    
    email = models.CharField(max_length=250, unique=True)
    passphrase= models.CharField(max_length=1834)
    pubk = models.CharField(max_length=400)
    privk = models.CharField(max_length=400)
   

@receiver(models.signals.post_save, sender = 'users.Registro')
def set_keys(sender, instance, **kwargs):
    if kwargs.get('created'):
        key = RSA.generate(2048)
        private_key = key.export_key(passphrase=instance.passphrase)
        f = open("static/private.pem","wb")
        f.write(private_key)
        f.close
        
        #sender.objects.filter(id = instance.id).update(privk = str(private_key))
        #print("Llave privada")
        public_key = key.publickey().export_key()
        sender.objects.filter(id = instance.id).update(pubk = str(public_key))
        print("Llave publica")
        
    
        

