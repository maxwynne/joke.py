import csv
import sys
from random import shuffle
import pyjokes

print(pyjokes.getjoke())

def joke1():
    joke1 = pyjokes.get_jokes(language='en', category='neutral')
    currentJoke = joke1

    print(joke1)

def joke2():
    joke2 = pyjokes.get_jokes(language='en', category='neutral')
    currentJoke = joke2

    print(joke2)

jokes = pyjokes.get_jokes(language='en', category='neutral')

for i in range(5):
    print(jokes[i])
