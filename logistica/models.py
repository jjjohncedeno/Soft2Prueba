from django.db import models

# Create your models here.

class Bus(models.Model):
  nDisco = models.IntegerField(blank=True , null = True)
  tipo = models.TextField(max_length=10,blank=True , null = True)
  marca = models.TextField(max_length=100,blank=True , null = True)
  placa = models.TextField(max_length = 7,blank=True , null = True)
  modelo = models.TextField(max_length = 30,blank=True , null = True)
  cSentados = models.IntegerField(blank=True , null = True)
  cParados = models.IntegerField(blank=True , null = True)

  def __unicode__(self):
    return unicode(self.placa)

  class Meta:
    verbose_name = "Bus"
    verbose_name_plural = "Buses"

class Conductor(models.Model):
  nombre = models.TextField(max_length=100)
  cedula = models.TextField(max_length=10)

  def __unicode__(self):
    return unicode(self.nombre)

  class Meta:
    verbose_name = "Conductor"
    verbose_name_plural = "Conductores"

class Ruta(models.Model):
  nombre = models.CharField(max_length=100)
  entrada="e"
  salida="s"
  tipos = (
    (entrada, 'Entrada'),
    (salida, 'Salida'),
  )

  tipo = models.CharField(max_length=2, choices = tipos, default = tipos)


  def __unicode__(self):
    return unicode(self.nombre)

  class Meta:
    verbose_name = "Ruta"
    verbose_name_plural= "Rutas"

class Horario(models.Model):
  ruta = models.ForeignKey(Ruta, related_name = 'Horario')
  bus = models.ForeignKey(Bus, related_name = 'Horario')
  conductor = models.ForeignKey(Conductor, related_name = 'Horario')
  fechaInicio = models.DateTimeField(auto_now = False)
  fechaFin = models.DateTimeField(auto_now = False)

  def __unicode__(self):
    return unicode(str(self.fechaInicio))

  class Meta:
    verbose_name = "Horario"
    verbose_name_plural= "Horarios"
