#un serializer permite poder llamar a un modulo especifico
#de RESTFRAMEWORK

from rest_framework import serializers

from .models import Usuarios, Productos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id','nombreUsuario', 'edadUsuario','direccionUsuario','fechaRegistro')
        read_only_fields = ('fechaRegistro',) #si solo es un elemento, debe ir una coma luego :D
        #read_only_fields es para solo lectura,
        # es decir no se puede modifical de ninguna forma tal columna
        


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('nombreProducto','tipoProducto','cantidadDisponibleProducto')
        