import random

def main():
    score=0
    level=get_level()
    for i in range(10):
        x,y= generate_integer(level)
        correct_answer=x+y
        for i in range(3):
            print(f"{x} + {y} = ")
            answer=int(input("enter your answer: "))
            if answer==correct_answer:
                score+=1
                break
            else:
                print("EEE")
                print(f"{x}+{y}={x+y}")

        print(f"current score: {score}")
    print(f"final score: {score}")


def get_level():
    while True:
        level=input("enter level: ")
        if level.isnumeric():
            if 1<=int(level)<=3:
                return int(level)
            break
        else:
            continue


def generate_integer(level):
    if level==1:
        x=random.randint(0,9)
        y=random.randint(0,9)

    elif level==2:
        x=random.randint(10,99)
        y=random.randint(10,99)

    elif level==3:
        x=random.randint(100,999)
        y=random.randint(100,999)

    return x,y


if __name__ == "__main__":
    main()
