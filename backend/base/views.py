
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products


@api_view(["GET"])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
    ]
    return Response(routes)

@api_view(["GET"])
def getProducts(request):
    return Response(products)

@api_view(["GET"])
def getProduct(request, pk):
    product = None
    for prod in products:
        if prod["_id"] == pk:
            product = prod
            break
    return Response(product)