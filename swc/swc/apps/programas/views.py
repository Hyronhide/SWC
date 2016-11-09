from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import *
from django.db.models import Q

# Create your views here.
def index_view (request):
    return render_to_response('programas/index.html' , context_instance = RequestContext(request) ) 
###################################### AREAS ###################################################
def Areas_View (request):
    lista_areas = Area.objects.filter(encargado = request.user)
    ctx = {'areas':lista_areas}
    return render(request, 'programas/areas.html', ctx)

def Programa_Area_View(request, id_area):
    lista_programas = Programa.objects.filter( area__nombre = id_area)
    area = Area.objects.get(nombre = id_area)
    #ctx = {'programas':lista_programas, 'area':area}    
    query = request.GET.get('q','')     
    if query:
        qset = (
            Q(nombre__icontains=query)|
            Q(codigo__icontains=query)
        )
        results = Programa.objects.filter(qset,area= area).distinct()  
        mostrar = False      
    else:
        mostrar = True
        results = []
    return render_to_response('programas/programas_areas.html', {
        "results": results,
        "query": query,
        "mostrar": mostrar,
        "programas": lista_programas, 
        "area": area,       
    },context_instance=RequestContext(request))

 

def Ficha_Programa_View(request, id_p): 
    lista_fichas = Ficha.objects.filter( programa__nombre = id_p)
    programa = Programa.objects.get(nombre = id_p)
    query = request.GET.get('q','')     
    if query:
        qset = (
            Q(identificador__icontains=query)|
            Q(programa__nombre__icontains=query)
        )
        results = Ficha.objects.filter(qset,programa= programa).distinct()  
        mostrar = False      
    else:
        mostrar = True
        results = []
    return render_to_response('programas/fichas_programas.html', {
        "results": results,
        "query": query,
        "mostrar": mostrar,
        "fichas": lista_fichas, 
        "programa": programa,       
    },context_instance=RequestContext(request))
    #ctx = {'fichas':lista_fichas, 'programa':programa}
    #return render_to_response('programas/fichas_programas.html', ctx, context_instance = RequestContext(request))



############################ PROGRAMAS ##########################################
def Programas_View(request):       
    lista_programas = Programa.objects.all()
    query = request.GET.get('q','')     
    if query:
        qset = (
            Q(nombre__icontains=query)|
            Q(codigo__icontains=query)
        )
        results = Programa.objects.filter(qset).distinct()  
        mostrar = False      
    else:
        mostrar = True
        results = []
    return render_to_response('programas/programas.html', {
        "results": results,
        "query": query,
        "mostrar": mostrar,
        "programas": lista_programas,        
    },context_instance=RequestContext(request))
    
def Single_Programa_View(request, id_p):
    programa = Programa.objects.get( nombre = id_p)
    ctx = {'programa':programa}
    return render(request, 'programas/single_programa.html', ctx)          

"""def Consultar_Programa_View(request):
    query = request.GET.get('q','')    
    if query:
        qset = (
            Q(nombre__icontains=query)|
            Q(codigo__icontains=query)
        )
        results = Programa.objects.filter(qset).distinct()  
        busqueda = True      
    else:
        busqueda = False
        results = []        
    return render_to_response('programas/programas.html', {
        "results": results,
        "query": query,
        "busqueda": busqueda,        
    },context_instance=RequestContext(request))     
"""
############################ FICHAS ##########################################  
def Fichas_View(request):
    lista_fichas = Ficha.objects.all()
    query = request.GET.get('q','') 
    mostrar = True     
    if query:
        qset = (
            Q(identificador__icontains=query)|
            Q(programa__nombre__icontains=query)
        )
        results = Ficha.objects.filter(qset).distinct()  
        mostrar = False      
    else:
        mostrar = True
        results = []
    return render_to_response('programas/fichas.html', {
        "results": results,
        "query": query,
        "mostrar": mostrar,
        "fichas": lista_fichas,        
    },context_instance=RequestContext(request))   

def Single_Ficha_View(request, id_f):
    ficha = Ficha.objects.get( identificador = id_f)
    ctx = {'ficha':ficha}
    return render(request, 'programas/single_ficha.html', ctx)

################################# BUSCADOR GENERAL ########################################## 

def Search_View(request):    
    query = request.GET.get('q','')         
    if query:
        qsetFichas = (
            Q(identificador__icontains=query)|
            Q(programa__nombre__icontains=query)
        )

        qsetProgramas = (
            Q(nombre__icontains=query)|
            Q(codigo__icontains=query)|
            Q(area__nombre__icontains=query)
        )

        resultsFichas = Ficha.objects.filter(qsetFichas).distinct()
        resultsProgramas = Programa.objects.filter(qsetProgramas).distinct()              
    else:
        resultsProgramas = []
        resultsFichas = []
    return render_to_response('programas/search.html', {
        "resultsFichas": resultsFichas,
        "resultsProgramas": resultsProgramas,
        "query": query,        
    },context_instance=RequestContext(request))          