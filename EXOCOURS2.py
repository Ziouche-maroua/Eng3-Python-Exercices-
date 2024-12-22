from math import sqrt
def contin() :    
    reply="yes"
    while reply=="yes":
        print("hi")
        reply=input("shall we continue ?   ")
    print("okay then")


def square():
    number=int(input("provide a number   "))
    if number<0:
        print("invalid number")
    elif number>0:
        sqt=sqrt(number)
    else: 
        exit

def exercice():
    num=int(input("Provide a positive number"))
    i=1
    
    while i<=num:
        j=1
        while j<=num:
            
            print(f"{i}*{j}")
            j=j+1
        i=i+1


def triangle():
    i=1
    while i<=10:
        print("*"*i)


triangle()
    



