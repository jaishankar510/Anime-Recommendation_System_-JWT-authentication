


from django.urls import path
from .views import RegisterView, LoginView, AnimeSearchView, AnimeRecommendationView, UserPreferencesView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('anime/search/', AnimeSearchView.as_view(), name='search_anime'),
    path('anime/recommendations/', AnimeRecommendationView.as_view(), name='anime_recommendations'),
    path('user/preferences/', UserPreferencesView.as_view(), name='user_preferences'),
]
