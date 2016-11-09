from django.conf.urls import patterns, url 
from .views import *

urlpatterns = [	
	
	#################################### AREAS ####################################################
	url(r'^areas/$',Areas_View,name = 'vista_areas'),
	url(r'^programas_areas/(?P<id_area>.*)/$',Programa_Area_View, name = 'vista_programa_area'),	
	url(r'^programa/(?P<id_p>.*)/$',Single_Programa_View, name = 'vista_single_programa'),
	url(r'^fichas_programas/(?P<id_p>.*)/$',Ficha_Programa_View, name = 'vista_ficha_programa'),
	url(r'^ficha/(?P<id_f>.*)/$',Single_Ficha_View, name = 'vista_single_ficha'),	
	################################################################################################
	###################################### PROGRAMAS ###################################################
	#url(r'^consultar_programa/$',Consultar_Programa_View,name='vista_consultar_programa'),
	url(r'^programas/$',Programas_View,name = 'vista_programas'),
	###################################### FICHAS ###################################################
	url(r'^fichas/$',Fichas_View,name = 'vista_fichas'),
	###################################### BUSCADOR GENERAL #########################################
	url(r'^search/$',Search_View,name = 'vista_search'),
	
]	