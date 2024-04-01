from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer

class NewGameView(APIView):
    """
    API endpoint to create a new game instance.
    """
    def post(self, request, format=None):
        """
        Handles POST request to create a new game instance.
        """
        game = Game.objects.create()
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GameStateView(APIView):
    """
    API endpoint to retrieve the state of an existing game instance.
    """
    def get(self, request, game_id, format=None):
        """
        Handles GET request to retrieve the state of an existing game instance.
        """
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GameSerializer(game)
        return Response(serializer.data)

class GuessView(APIView):
    """
    API endpoint to make a guess in an existing game instance.
    """
    def post(self, request, game_id, format=None):
        """
        Handles POST request to make a guess in an existing game instance.
        """
        try:
            game = Game.objects.get(pk=game_id)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if 'guess' not in request.data:
            return Response({"error": "Guess character is missing"}, status=status.HTTP_400_BAD_REQUEST)

        letter = request.data['guess'].lower()
        game.guess_letter(letter)

        serializer = GameSerializer(game)
        return Response(serializer.data)

class RootView(APIView):
    """
    Root API endpoint providing general information about the Hangman API.
    """
    def get(self, request, format=None):
        """
        Handles GET request to provide general information about the Hangman API.
        """
        content = {'message': 'Welcome to Hangman API. Use /game/new/ to start a new game, /game/<game_id>/ to get the game state, and /game/<game_id>/guess/ to make a guess.'}
        return Response(content)
