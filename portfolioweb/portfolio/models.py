from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = CKEditor5Field('Descripción',config_name='default',blank=True,null=True)
    image = models.ImageField(upload_to='projects', blank=True, null=True, verbose_name="Imagen")
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name= "Fecha de actualizacion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["created"]
        

    def __str__(self):
        return self.title
