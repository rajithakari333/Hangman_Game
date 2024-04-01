from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for the Game model, providing a JSON representation of game data.
    """
    # Additional fields to include in the serialized representation
    masked_word = serializers.ReadOnlyField()  # Representing the word with guessed letters revealed
    game_state = serializers.ReadOnlyField()   # Representing the current state of the game

    class Meta:
        model = Game
        # Fields to include in the serialized representation
        fields = ['id', 'masked_word', 'incorrect_guesses', 'incorrect_guesses_allowed', 'game_state', 'guessed_letters']
        # Fields that should be read-only in the serialized representation
        read_only_fields = ['id', 'masked_word', 'incorrect_guesses', 'game_state']
