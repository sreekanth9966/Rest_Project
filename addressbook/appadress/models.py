from django.db import models

#AddressBook Model
class addressModel(models.Model):
    Name=models.CharField(max_length=(100))
    Age=models.IntegerField()
    Native_Place=models.CharField(max_length=(100))
    Pincode=models.IntegerField()