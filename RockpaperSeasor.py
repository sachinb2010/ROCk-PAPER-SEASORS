import random


def game(comp, userinput):


    if comp==userinput:
        return None

    elif comp=='R' and userinput=='S':
        return False

  


    elif comp=='P' and userinput=="R":
        return False

    elif comp=='S' and userinput=='P':
        return False
    
    elif comp=='S' and userinput=='R':
        return True

  


    elif comp=='R' and userinput=="P":
        return True

    elif comp=='P' and userinput=='S':
        return True

        
num=random.randint(1,3)
if num==1:
    comp= 'R' 
    

elif num==2:
    comp = 'P' 

elif num==3:
    comp ='S'



print("  R for Stone P for paper S Seasor ")
print("Enter all Input in Capital Letters :   ")
userinput=input("enter Your Choice")



winner=game(comp,userinput)
if winner=="none":
    print("Tie ")
if winner:
    print("You win")
else:
    print("you lose")
