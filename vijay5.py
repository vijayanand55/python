import random
while(1):
    r=input("Do you Want to Play the Game:")
    if(r=="Yes" or r=="YES" or r=="yes"):
        y=random.randint(1,6)
        print(y)
    elif(r=="NO" or r=="No" or r=="No"):
        print("Thanks for Playing the Game")
        break
    
