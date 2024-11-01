from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

@api_view(["GET"])
def endpoints(request):
    data = {
        'locahost' : 'List of Endpoints',
        'api/token/' : 'Login Authentication',
        'api/token/refresh/' : 'Refresh Authentication',
        'users/' : 'Create a users account',
        'usersProfile/' : 'Create a users profile',
        'usersProfile/update/' : 'Update,delete and get a particular users profile',
        'RoomCategory/' : 'get a roomcategory',
        'Room/' : 'update,delete and get a particular room',
        'Booking/' : 'get a booking process'
    }

    returnResponse(data)



class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer


class UserProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileserializers


class UserProfileUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileserializers
    lookup_field = 'pk'


class RoomCategory(generics.ListAPIView):
    queryset = RoomCategory.objects.all()
    serializer_class = RoomCategoryserializers


class Room(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = Roomserializer
    lookup_field = 'pk'


class Booking(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = Bookingserializers






