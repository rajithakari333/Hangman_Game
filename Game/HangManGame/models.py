import random
from django.db import models

class Game(models.Model):
    """
    Represents a game of Hangman.
    """
    WORD_CHOICES = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]

    word = models.CharField(max_length=100)
    incorrect_guesses_allowed = models.PositiveSmallIntegerField(default=0)
    incorrect_guesses = models.PositiveSmallIntegerField(default=0)
    guessed_letters = models.CharField(max_length=26, blank=True)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to set default values for certain attributes and choose a random word if not provided.
        """
        if not self.id:
            self.word = random.choice(Game.WORD_CHOICES)
            if len(self.word) <= 4: 
                self.incorrect_guesses_allowed = 2
            else:
                self.incorrect_guesses_allowed = max(1, len(self.word) // 2)
        super().save(*args, **kwargs)

    @property
    def masked_word(self):
        """
        Returns the word with guessed letters revealed and others masked with underscores.
        """
        return ''.join(letter if letter.lower() in self.guessed_letters.lower() else '_' for letter in self.word)

    @property
    def game_state(self):
        """
        Returns the current state of the game: 'Won', 'Lost', or 'InProgress'.
        """
        if self.is_won:
            return 'Won'
        elif self.is_lost:
            return 'Lost'
        else:
            return 'InProgress'

    @property
    def is_won(self):
        """
        Checks if the game is won, i.e., all letters in the word have been guessed.
        """
        return set(self.word.lower()).issubset(set(self.guessed_letters.lower()))

    @property
    def is_lost(self):
        """
        Checks if the game is lost, i.e., the number of incorrect guesses exceeds the limit.
        """
        return self.incorrect_guesses >= self.incorrect_guesses_allowed

    def guess_letter(self, letter):
        """
        Allows the player to guess a letter. Updates game state accordingly.
        """
        letter = letter.lower()  # Convert to lowercase
        if letter not in self.guessed_letters.lower():
            self.guessed_letters += letter
            if letter not in self.word.lower():
                self.incorrect_guesses += 1
        self.save()
