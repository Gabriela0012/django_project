from django.shortcuts import render, HttpResponse
from stock.models import Insumo, Producto

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