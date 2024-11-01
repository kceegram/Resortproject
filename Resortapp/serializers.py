from .models import *
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password',]


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserProfileserializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class RoomCategoryserializers(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = '__all__'


class Roomserializer(serializers.ModelSerializer):
    class Meta:
        model = Room 
        fields = '__all__'


class Bookingserializers(serializers.ModelSerializer):
    class Meta:
        models = Booking 
        fields = '__all__'


    