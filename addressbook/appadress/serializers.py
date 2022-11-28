from .models import *
from rest_framework import serializers




class AddressBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=addressModel
        fields='__all__'
        
