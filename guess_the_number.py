import random
import sys

while True:
    n=int(input("enter level: "))

    if n<0:
        continue
    else:
        break

m=random.randint(1,n)

while True:
    try:
        guess=int(input("Guess: "))
        if guess<0:
            continue
        if 0<guess<m:
            print("too small!")
        elif guess>m:
            print("too large!")
        elif guess==m:
            print("just right!")
            break
    except ValueError:
        continue
