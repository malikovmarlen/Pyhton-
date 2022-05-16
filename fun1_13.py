
def num(a,q,t):
    print("Take a guess.")
    t+=1
    n=int(input())
    if n!=a:
        print("Your guess is too low.")
        num(a,q,t)
    else:
         print("Good job,",q,"! You guessed my number in",t,"guesses!")
print("Hello! What is your name?")
q=str(input())
print("Well,",q,", I am thinking of a number between 1 and 20.")
from random import randint
a=randint(1,21)
t=0
num(a,q,t)
