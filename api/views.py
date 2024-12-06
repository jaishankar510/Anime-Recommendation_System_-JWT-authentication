


import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Anime, UserPreferences
from .serializers import UserSerializer, AnimeSerializer, UserPreferencesSerializer

# URL for AniList GraphQL API
ANI_LIST_API_URL = "https://graphql.anilist.co/"

# Function to search anime via AniList API
def search_anime(query):
    query_string = """
    query ($search: String) {
      Media(search: $search, type: ANIME) {
        id
        title {
          romaji
        }
        genres
        description
      }
    }
    """
    variables = {"search": query}
    response = requests.post(ANI_LIST_API_URL, json={"query": query_string, "variables": variables})
    return response.json()

# RegisterView - Handles user registration
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                "access_token": access_token,
                "refresh_token": str(refresh),
                "detail": "User created successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LoginView - Handles user login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is None:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return Response({
            "access_token": access_token,
            "refresh_token": str(refresh),
        }, status=status.HTTP_200_OK)

# AnimeSearchView - Allows searching anime based on a query string
class AnimeSearchView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        anime_data = search_anime(query)
        return Response(anime_data)

# AnimeRecommendationView - Recommends anime based on user preferences
class AnimeRecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        preferences = UserPreferences.objects.get(user=user)
        favorite_genre = preferences.favorite_genre

        # Fetch anime recommendations based on favorite genre
        anime_data = search_anime(favorite_genre)
        return Response(anime_data)

# AnimeCreateView - Create new anime entry
class AnimeCreateView(APIView):
    def post(self, request):
        serializer = AnimeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new anime data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# UserPreferencesView - Allows getting and updating user preferences
class UserPreferencesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        preferences = UserPreferences.objects.get(user=user)
        serializer = UserPreferencesSerializer(preferences)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        preferences = UserPreferences.objects.get(user=user)

        # Update favorite genre and watched anime
        favorite_genre = request.data.get('favorite_genre')
        watched_anime_ids = request.data.get('watched_anime', [])

        preferences.favorite_genre = favorite_genre
        preferences.watched_anime.set(Anime.objects.filter(id__in=watched_anime_ids))
        preferences.save()

        serializer = UserPreferencesSerializer(preferences)
        return Response(serializer.data)

