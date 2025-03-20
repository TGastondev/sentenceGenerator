""" 
Chapter 4 Case Study (Pages 129 - 131)
Program: sentenceGenerator.py
3/5/2025

Application that generates and displays sentences using simple grammar and vocabulary. Words are chosen at random. Each small task will be its own function ad user will enter the number of sentences to generate.
"""

import random

# Global variables containing the different parts of speech that all functions can use 
articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL", "DOG", "CAT", "TURTLE", "ROCK", "PIZZA", "ABRAHAM LINCOLN", "MAZDA", "TABLE", "LAPTOP")

verbs = ("HIT", "SAW", "LIKED", "JUMPED", "SNEEZED", "RAN", "FELL", "TYPED", "SLAPPED")

prepositions = ("WITH", "BY", "FROM", "AT", "TO", "UNDER", "AROUND")

# Definitions of the sentence() function
def sentence():
	"""Builds and returns a sentence. """
	return nounPhrase() + " " + verbPhrase()

# Definition of the nounPhrase() function
def nounPhrase():
	"""Builds and returns a noun phrase."""
	return random.choice(articles) + " " + random.choice(nouns)

# Definition of the verbPhrase() function
def verbPhrase():
	""" Builds and returns a verb phase. """
	return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

# Definition of the prepositionalPhrase() function
def prepositionalPhrase():
	""" Builds and returns a prepositional phrase."""
	return random.choice(prepositions) + " " + nounPhrase()

# Definition of the main() function
def main():
	"""Allows the user to input the number of sentences."""
	number = int(input("Enter the number of sentences: "))
	for count in range(number):
		print(sentence())
	input("\nSentences complete, press ENTER to exit..")

# Global call to main() for program to execute
if __name__ == '__main__':
		main()