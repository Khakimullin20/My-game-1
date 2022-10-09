'''
import random


R="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

P="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

S="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
a =[R,P,S]
print(a[0],a[1], a[2])

while True:

    user  = int(input("What your choice? 0 - r, 1 - p, 2 - s:"))
    print(a[user])
    comp = random.randint(0,2)
    print(a[comp])
    if user == 2 and comp == 0:
        print("uer lose")


    elif comp == 2 and user == 0:
        print("user win")


    elif user>comp:
        print("user win ")


    elif comp>user:
        print("computer win")



    elif comp == user:
        print("Tie")'''












def func(q,w):
    print(q-w)
    print(q+w)
    print(q/w)
    print(q*w)
    print("       ")

func(3,2)    
func(5,6)
func(7,8)


































    






