from django.shortcuts import render, HttpResponse
from stock.models import Insumo, Producto
from django.template import loader
from stock.forms import InsumoFormulario

# Create your views here.
def crear_producto(request):
    if request.method == 'POST':
        nuevo_producto = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            cantidad_de_stock = request.POST["cantidad_de_stock"],
            otra_cosa = request.POST["otra_cosa"]
        )
        nuevo_producto.save()
        return render(request, "index.html")
    
    return render(request, "producto_form.html")

def crear_insumo(request):
    
    if request.method == 'POST':
        nuevo_formulario = InsumoFormulario(request.POST)
        print(nuevo_formulario)
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            insumo = Insumo(
                nombre = informacion["nombre"],
                descripcion = informacion["descripcion"],
                unidad_de_medida = informacion["unidad_de_medida"],
                cantidad_de_stock = informacion["cantidad_de_stock"]
             )
            insumo.save()
            return render(request, "index.html")            
    else:
        nuevo_formulario = InsumoFormulario()
        return render(request, "insumo_formulario.html", {"formulario": nuevo_formulario})