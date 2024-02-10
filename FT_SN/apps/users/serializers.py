from rest_framework import serializers
from .models import User

class UserCreateSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=('Jugador','Organizador'))
    
    class Meta:
        model = User
        fields = ('username','email','birthdate','role')
        
    def create(self,validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        
        if role == 'Organizador':
            user = User.objects.create_owner(password=password, **validated_data)
        else:
            user = user = User.objects.create_player(password=password, **validated_data)
        return user