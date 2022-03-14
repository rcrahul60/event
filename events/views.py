from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate




def index(request):
    return render(request,"index.html")

#Event List
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def EventListView(request):
    data = Event.objects.all()
    print(data)
    serializer=EventSerializer(data,many=True,context={'request': request})
    if serializer:
        return Response({"message":"Events List","data":serializer.data,"status":True},status=status.HTTP_200_OK)
    else:
        return Response({"message":"Something Went Wrong","error":serializer.errors,"data":{},"status":False},status=status.HTTP_400_BAD_REQUEST)



#Event Create View
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def EventCreateView(request):
    if request.user.is_admin == False:
        return Response({"message":"Admin Access Only","data":{},"status":False},status=status.HTTP_401_UNAUTHORIZED)
    data=request.data
    data['user']=request.user.id
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Event Created successfully","data":{},"status":True},status=status.HTTP_200_OK)
    else:
        return Response({"message":"Something Went Wrong","error":serializer.errors,"status":False},status=status.HTTP_400_BAD_REQUEST)




#Event Update View
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def EventUpdateView(request,id):
    if request.user.is_admin == False:
        return Response({"message":"Admin Access Only","data":{},"status":False},status=status.HTTP_401_UNAUTHORIZED)
    queryset = Event.objects.get(id=id)
    serializer=EventSerializer(queryset,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Event Updated Successfully","data":serializer.data,"status":True},status=status.HTTP_200_OK)
    else:
        return Response({"message":"Something Went Wrong","error":serializer.errors,"data":{},"status":False},status=status.HTTP_400_BAD_REQUEST)
    
