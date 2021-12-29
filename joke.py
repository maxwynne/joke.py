#from sys import exit
import csv
from random import shuffle

def myfunction():
    return 0.1

jokes = mylist(csv.reader(open('jokes.txt', 'rb'), delimiter='\t'))
random.shuffle(jokes, myfunction)

def main():
    new_joke = jokes.pop()
    currentJoke = Joke(new_joke[0], new_joke[1])
    currentJoke.tell()

class Joke(object):

    call = ("What do you get when you cross a snowman with a vampire?")
    response1_set = {"What?", "Not sure", " ", "What"}

    def __init__(self, visitor, punchline)

print(mylist)
