from shopsmart.models import Usuarios, Productos
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer, ProductoSerializer



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all() 
    #objets.all consulta todos los datos que existan en una tabla
    permission_classes = [permissions.AllowAny]
    #AllowAny = cualquier app/cliente puede hacer peticiones al servidor/app
    serializer_class = UsuarioSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer
