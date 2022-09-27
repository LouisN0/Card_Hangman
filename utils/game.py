#importing the random module (helps to randomise things)
import random
#creation of the class Hangman
class Hangman:

    possible_words = ['becode', 'learning', 'mathematics', 'sessions']
    #this is the constructor, it is where you put the fundamentals variabels and there value for the game to start
    def __init__(self) -> None:
        #it choose a random word in the list possible_world
        self.word_to_find = list(random.choice(self.possible_words))
        self.lives = 5
        #creating an array with the exact same number of "_" that there is letter in the wordt_to_find
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
    #creating a play function, this is the function principal
    def play(self):
        letter = input('enter a letter: ')
        #it check if the letter is a letter or if it is not more than 2 letter 
        while not letter.isalpha() or len(letter) != 1:
            letter = input(f'enter a letter: ')
        #this is the part that check if the letter is in the word
        if letter not in self.word_to_find:
            self.error_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(letter)
            print('wrong !!')
            print(f'wrongly guessed letters: {self.wrongly_guessed_letters}')
        #here it is if the letter is in the word 
        else:
            for i in range(len(self.word_to_find)):
                if self.word_to_find[i] == letter:
                    self.correctly_guessed_letters[i] = letter
                    
            print(f"well done, you have find the letter {letter}!")
        #add a turn if we are done with all the checks
        self.turn_count += 1       
    #this is the function that is activate at the end if tou have loose the game, it check the player want a rematch or not
    def game_over(self):
        print('game over, you have no more lives')
        rematch = input('Do you want to play again ?')
        if rematch == "yes" or rematch == "y":
            print("You hate to loose don't you ?")
            return self.start_game()
        else:
            return print('okay, have a grate day :)')
    #this is the function that is activate if the player win, it check the player want a rematch or not
    def well_played(self):
        print(f'You found the word: {"".join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!')
        rematch = input('Do you want to play again ?')
        if rematch == "yes" or rematch == "y":
            print("great, lets play !")
            return self.start_game()
        else:
            return print('okay, have a grate day :)')
    #this is the function that start the game
    def start_game(self):
        #put all the variable back to there original state (this why the __init__ is usefull)
        self.__init__()
        #this part is gonna loop to check if there is still "_" in the well_guessed_letter until there is no more "_"
        while "_" in self.correctly_guessed_letters:
            #if no live game end
            if self.lives == 0:
                return self.game_over()
            else:
                self.play()
                print(f'well guessed letters: {self.correctly_guessed_letters}')
                print(f'bad guessed letters: {self.wrongly_guessed_letters}')
                print(f'lives : {self.lives}')
                print(f'numbers of errors: {self.error_count}')
                print(f'number of turn {self.turn_count}')
        #when there is gonna be no more "_" the function is gonna return the well_played function
        return self.well_played()