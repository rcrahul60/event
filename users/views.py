from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate


# register
@api_view(["POST"])
@permission_classes([AllowAny])
def RegistrationView(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get_or_create(user=user)[0].key
        return Response({'message':"user created successfully","token":token,"status":True},status=status.HTTP_201_CREATED)
    else:
        return Response({"message":"Something Went Wrong","error":serializer.errors,"status":False},status=status.HTTP_400_BAD_REQUEST)


#Login
@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    try:
        user = authenticate(email = email,password=password)
        if user.is_active:
            token = Token.objects.get_or_create(user=user)[0].key
            return Response({"message":"login successfull","token":token,"status":True},status=status.HTTP_200_OK)
        else:
            return Response({"message":"please check you email and password","data":{},"status":False},status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"message":"login failed","data":{},"status":False},status=status.HTTP_400_BAD_REQUEST)


