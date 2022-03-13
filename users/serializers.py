from .models import *
from rest_framework import serializers
from django.conf import settings


#Registration Serializer
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password','is_admin']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            is_admin=validated_data['is_admin'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
