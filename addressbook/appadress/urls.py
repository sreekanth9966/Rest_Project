
from django.urls import path
from .views import *

urlpatterns = [
    

    path('get/',getaddress),
    path('post/',postaddress),
    path('update/<int:id>/',updateaddress),
    path('delete/<int:id>/',deleteaddress),
    
]


