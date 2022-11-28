from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import*

# Create your views here.


@api_view(['GET'])
def getaddress(request):
    addressobj=addressModel.objects.all()
    serialize=AddressBookSerializer(addressobj,many=True)
    return Response(serialize.data)
    

@api_view(['POST'])
def postaddress(request):
    addressobj=addressModel.objects.all()
    serialize=AddressBookSerializer(data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)
    
@api_view(['POST'])
def updateaddress(request,id):
    addressobj=addressModel.objects.get(id=id)
    serialize=AddressBookSerializer(instance=addressobj,data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)

@api_view(['DELETE'])
def deleteaddress(request,id):
    addressobj=addressModel.objects.get(id=id)
    addressobj.delete()
    return Response("item is deleted")
    