# api/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Anime, UserPreferences

# Serializer for user registration and login
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Serializer for anime data
class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

# Serializer for user preferences (favorite genres and watched anime)
class UserPreferencesSerializer(serializers.ModelSerializer):
    watched_anime = AnimeSerializer(many=True)

    class Meta:
        model = UserPreferences
        fields = ['id', 'user', 'favorite_genre', 'watched_anime']
