from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TIPO_PROGRAMA = (
	('regular','Regular'),
	('especial', 'Especial'),
	)

ESTADO_CURSO = (
	('en_ejecucion', 'En ejecucion'),
	('terminada', 'Terminada'),
	('terminada_por_fecha', 'Terminada por fecha'),
	)

JORNADA = (
	('diurna', 'Diurna'),
	('mixta', 'Mixta'),
	)

TIPO_FORMACION = (
	('a_la_medida', 'A la medida'),
	('no_a_la_medida', 'No a la medida'),
	)

ETAPA = (
	('lectiva', 'Lectiva'),
	('practica', 'Practica'),
	)

MODALIDAD = (
	('presencial', 'Presencial'),
	('virtual', 'Virtual'),
	)

TIPO_IDENTIFICACION_EMPRESA = (
	('nit','NIT'),
	('its','ITS'),
	('cc','CC'),
	)

AMPLIACION_COBERTURA = (
	('s','S'),
	('n','N'),
	)

class Area(models.Model):

	nombre 		= models.CharField(max_length = 40)
	encargado 	= models.ForeignKey(User)

	def __unicode__(self):
		return self.nombre

class Sector(models.Model):

	nombre = models.CharField(max_length = 30)
	codigo = models.CharField(max_length = 11)

	def __unicode__(self):
		return self.nombre

class Sector_Nuevo(models.Model):

	nombre = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.nombre		

class Pais(models.Model):

	nombre = models.CharField(max_length = 50)
	codigo = models.CharField(max_length = 11)

	def __unicode__(self):
		return self.nombre	

class Departamento(models.Model):

	nombre 	= models.CharField(max_length = 50)
	codigo 	= models.CharField(max_length = 11)
	pais 	= models.ForeignKey(Pais)

	def __unicode__(self):
		return self.nombre	

class Municipio(models.Model):

	nombre 			= models.CharField(max_length = 50)
	codigo 			= models.CharField(max_length = 11)
	departamento 	= models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.nombre	

class Centro_Formacion(models.Model):

	nombre 		= models.CharField(max_length = 100)
	codigo 		= models.CharField(max_length = 11)
	municipio 	= models.ForeignKey(Municipio)

	def __unicode__(self):
		return self.nombre

class Nivel_Formacion(models.Model):

	nombre = models.CharField(max_length = 50)
	codigo = models.CharField(max_length = 11)

	def __unicode__(self):
		return self.nombre

class Ocupacion(models.Model):

	nombre = models.CharField(max_length = 120)
	codigo = models.CharField(max_length = 11)

	def __unicode__(self):
		return self.nombre	

class Tipo_Programa(models.Model):	

	nombre = models.CharField(max_length = 50)
	codigo = models.CharField(max_length = 11)

	def __unicode__(self):
		return self.nombre

class Empresa(models.Model):	

	nombre 					= models.CharField(max_length = 50)
	#no tiene codigo
	
	tipo_identificacion		= models.CharField(max_length = 3, choices = TIPO_IDENTIFICACION_EMPRESA)
	numero_identificacion	= models.CharField(max_length = 20)

	def __unicode__(self):
		return self.nombre	
		

class Programa(models.Model):

	nombre 				= models.CharField(max_length = 250)
	codigo 				= models.CharField(max_length = 11)
	version 			= models.CharField(max_length = 11)
	duracion 			= models.IntegerField()
	tipo 				= models.CharField(max_length = 10, choices = TIPO_PROGRAMA)	
	area 				= models.ForeignKey(Area)
	centro_formacion 	= models.ForeignKey(Centro_Formacion)
	ocupacion 			= models.ForeignKey(Ocupacion)
	sector 				= models.ForeignKey(Sector)
	nuevo_sector 		= models.ForeignKey(Sector_Nuevo)
	nivel_de_formacion 	= models.ForeignKey(Nivel_Formacion)
	tipo_programa 		= models.ManyToManyField(Tipo_Programa)


	def __unicode__(self):
		return "%s - Codigo: %s - Version: %s" % (self.nombre, self.codigo, self.version)


class Convenio(models.Model):	

	nombre 		= models.CharField(max_length = 50)
	codigo 		= models.CharField(max_length = 11)
	programa 	= models.ForeignKey(Programa)
	empresa  	= models.ForeignKey(Empresa)

	def __unicode__(self):
		return self.nombre	
		
################################################################################################

class Competencia(models.Model):	

	nombre 		= models.CharField(max_length = 100)
	codigo 		= models.CharField(max_length = 11)
	fase		= models.CharField(max_length = 50)
	programa 	= models.ForeignKey(Programa)

	def __unicode__(self):
		return self.nombre

class Resultado_Aprendizaje(models.Model):	

	nombre 		= models.CharField(max_length = 50)
	codigo 		= models.CharField(max_length = 11)
	competencia = models.ForeignKey(Competencia)

	def __unicode__(self):
		return self.nombre		

class Responsable(models.Model):	

	nombre 		         = models.CharField(max_length = 30)
	numero_identificador = models.CharField(max_length = 11)
	
	def __unicode__(self):
		return self.nombre	
'''
class Contrato(models.model):	

	codigo 				= models.CharField(max_length = 11)
	tipo 				= models.CharField(max_length = 11)
	fecha_inicio 		= models.DateField(null = False, max_length = 50)
	fecha_terminacion 	= models.DateField(null = False, max_length = 50)

	def __unicode__(self):
		return self.tipo				

class Instructor(models.model):	

	tipo_identificacion 	= models.CharField(max_length = 20)
	numero_identificacion 	= models.CharField(max_length = 20)
	nombres 				= models.CharField(max_length = 50)
	apellidos 				= models.CharField(max_length = 50)
	correo 					= models.CharField(max_length = 50)
	celular 				= models.CharField(max_length = 10)
	direccion 				= models.CharField(max_length = 30)
	estado 					= models.CharField(max_length = 10)
	cod_centro_formacion	= models.CharField(max_length = 11)
	contratos 				= models.ManyToManyField(Contrato)


	def __unicode__(self):
		return self.nombres		
'''
class Ficha(models.Model):

	identificador 				= models.CharField(max_length = 11)
	identificador_unico 		= models.CharField(max_length = 11)
	estado 						= models.CharField(max_length = 20, choices = ESTADO_CURSO)
	jornada 					= models.CharField(max_length = 10, choices = JORNADA)
	tipo_formacion 				= models.CharField(max_length = 20, choices = TIPO_FORMACION)
	fecha_inicio				= models.DateField(null = False, max_length = 50)
	fecha_terminacion			= models.DateField(null = False, max_length = 50)
	etapa 						= models.CharField(max_length = 20, choices = ETAPA)
	modalidad 					= models.CharField(max_length = 20, choices = MODALIDAD)
	ampliacion_cobertura 		= models.CharField(max_length = 1, choices = AMPLIACION_COBERTURA)
	numero_cursos 				= models.IntegerField()
	total_aprendices_masculinos = models.IntegerField()
	total_aprendices_femeninos 	= models.IntegerField()
	toal_aprendices 			= models.IntegerField()
	horas_contratistas 			= models.IntegerField()
	horas_contratistas_externos = models.IntegerField()
	horas_monitores 			= models.IntegerField()
	horas_inst_empresa 			= models.IntegerField()
	total_horas 				= models.IntegerField()
	total_aprendices_activos 	= models.IntegerField()
	programa_especial 			= models.CharField(max_length = 50)
	programa 					= models.ForeignKey(Programa)
	responsable 				= models.ForeignKey(Responsable)
	#instructores 				= models.ManyToManyField(Instructor)

	def __unicode__(self):
		return "%s - Programa: %s" % (self.identificador, self.programa.nombre)