import random
x = 0
def makeNew():
    x = random.randint(0,1000)
    return x
def guess(y):
    if y>x: 
        print("Try Lesser")
        return 1
    elif x>y: 
        print("Try Greater")
        return  -1
    else: 
        print(f"You Got it !! It was {x}")
        return 0
while True:
    x = makeNew()
    while True:
        try:
            i = int(input("Take a Guess::"))
            if (guess(i)):
                continue
            else:
                break
        except:
            print("Not a integer")
    n = input("Try Again:y/n?")
    if n == 'y':
        continue
    else:
        break
        
