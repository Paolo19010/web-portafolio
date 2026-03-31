from django.db import models

# Create your models here.
class Information(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Nombre")
    title = models.CharField(max_length=200, verbose_name="Titulo")
    image = models.ImageField(upload_to='information', blank=True, null=True, verbose_name="Imagen")
    resume = models.TextField(blank=True, verbose_name= "Resumen")
    desc_contact = models.TextField(blank=True, verbose_name= "Resumen de contacto")
    cell = models.CharField(max_length=10)
    email = models.EmailField(verbose_name="Email")
    honorarios = models.CharField(max_length=200, verbose_name="Honorarios")

    class Meta:
        verbose_name = "informacion"
        verbose_name_plural = "informacion"

        

    def __str__(self):
        return self.Name
    
class Background(models.Model):
    portadaImage = models.ImageField(upload_to='backgorund', blank=True, null=True, verbose_name="Fondo de portada")
    acercaDeImage = models.ImageField(upload_to='backgorund', blank=True, null=True, verbose_name="Fondo de Acerca de")
    portafolioImage = models.ImageField(upload_to='backgorund', blank=True, null=True, verbose_name="Fondo de portafolio")
    contactImage = models.ImageField(upload_to='backgorund', blank=True, null=True, verbose_name="Fondo de contacto")
