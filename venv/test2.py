def isEqual(num1,num2):
    if(num1<num2):
        print("small")
        return False;
    if(num1>num2):
        print("big")
        return False;
    if(num1==num2):
        print("bingo")
        return True;

from random import randint
num=randint(1,10)
print("guess what I think?")
bingo=False
while bingo==False:
    answser=int(input())
    bingo=isEqual(answser,num)

