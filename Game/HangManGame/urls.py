from django.urls import path
from .views import NewGameView, GameStateView, GuessView

urlpatterns = [
    # Endpoint to create a new game instance
    path('game/new/', NewGameView.as_view(), name='new_game'),

    # Endpoint to retrieve the state of an existing game instance
    # 'game_id' is the ID of the game instance to retrieve
    path('game/<int:game_id>/', GameStateView.as_view(), name='game_state'),

    # Endpoint to make a guess in an existing game instance
    # 'game_id' is the ID of the game instance to make the guess in
    path('game/<int:game_id>/guess/', GuessView.as_view(), name='guess'),
]
