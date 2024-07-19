import random

class HangmanGame:
    def __init__(self):
        self.secretWord = self.get_random_word()
        self.currentWord = '_' * len(self.secretWord)
        self.attemptsLeft = 5

    def play(self):
        print("Welcome to Hangman!")
        print("Category: Sports")
        print(f"You have {self.attemptsLeft} attempts to guess the sport name.")

        while self.attemptsLeft > 0:
            self.display_game_info()
            guess = input("Guess a letter: ").lower()

            if guess.isalpha():
                if self.already_guessed(guess):
                    print("You've already guessed that letter.")
                else:
                    correct_guess = self.update_current_word(guess)
                    if correct_guess:
                        print("Good guess!")
                        if self.currentWord == self.secretWord:
                            self.display_game_info()
                            print(f"Nice! You guessed the word: {self.secretWord}")
                            return
                    else:
                        print("Incorrect guess.")
                        self.attemptsLeft -= 1
            else:
                print("Invalid input. Please enter a valid letter.")

        print(f"Out of attempts! The word was: {self.secretWord}")

    def get_random_word(self):
        words = ["basketball", "soccer", "football", "tennis", "swimming"]
        return random.choice(words)

    def already_guessed(self, letter):
        return letter in self.currentWord

    def update_current_word(self, guess):
        correct_guess = False
        for i in range(len(self.secretWord)):
            if self.secretWord[i] == guess:
                self.currentWord = self.currentWord[:i] + guess + self.currentWord[i + 1:]
                correct_guess = True
        return correct_guess

    def display_game_info(self):
        print(f"Current word: {self.currentWord}")
        print(f"Attempts left: {self.attemptsLeft}")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()