from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User

class Serializers(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

    def create(self, validate_data):
        instance = Permission()
        instance.name = validate_data.get("name")
        instance.description = validate_data.get("description")
        instance.estado = validate_data.get("estado")
        instance.save()
        return instance

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'password', 'is_staff')
       

    
    