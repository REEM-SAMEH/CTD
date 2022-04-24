import cv2
import random
bag1=['*','*','*','*','*','*','*','*','*','*']
bag2=['*','*','*','*','*','*','*','*','*','*']
bag3=['*','*','*','*','*','*','*','*','*','*']
f=1
while True:
    if len(bag1)==0 and len(bag2)==0 and len(bag3)==0 and f==1:
        img = cv2.imread(r"C:\Users\En\OneDrive\Desktop\ctd\ylose.jpeg", cv2.IMREAD_COLOR)
        cv2.imshow("you lose", img)
        cv2.waitKey(0)
        break
    while f==1 :
        print(len(bag1),len(bag2),len(bag3))
        x=int(input("which bag? "))
        y=int(input("number of balls "))
        if x==1:
            if(len(bag1)>0): 
                if(y>0 and y<6):
                    if(len(bag1)>=y):
                        for i in range (y) :
                             bag1.remove('*')
                             f=0
                    else:
                         print("bag lenght less than ")
                else:
                     print("please choose from 1 to 5")
            else:
                 print("bag empty choose anthor")
        elif x==2:
            if(len(bag2)>0): 
                if(y>0 and y<6):
                    if(len(bag2)>=y):
                        for i in range (y) :
                             bag2.remove('*')
                             f=0
                    else:
                         print("bag lenght less than ")
                else:
                     print("please choose from 1 to 5")
            else:
                 print("bag empty choose anthor")
        elif x==3:
            if(len(bag3)>0): 
                if(y>0 and y<6):
                    if(len(bag3)>=y):
                        for i in range (y) :
                             bag3.remove('*')
                             f=0
                    else:
                         print("bag lenght less than ")
                else:
                     print("please choose from 1 to 5")
            else:
                 print("bag empty choose anthor")
        else:
             print("bag from 1 to 3")
    if len(bag1)==0 and len(bag2)==0 and len(bag3)==0 and f==0:
        img = cv2.imread(r"C:\Users\En\OneDrive\Desktop\ctd\ywin.jpeg", cv2.IMREAD_COLOR)
        cv2.imshow("you win", img)
        cv2.waitKey(0)
        break
    while f==0 :
        print("you removed ", y, "from bag ", x)
        print(len(bag1),len(bag2),len(bag3))
        compbag=random.randint(1,3)
        compballs=random.randint(1,5)
        if compbag==1 and len(bag1)>0 and len(bag1)>=compballs:
            for i in range (compballs) :
                bag1.remove('*')
                f=1
        if compbag==2 and len(bag2)>0 and len(bag2)>=compballs:
            for i in range (compballs) :
                bag2.remove('*')
                f=1
        if compbag==3 and len(bag3)>0 and len(bag3)>=compballs:
            for i in range (compballs) :
                bag3.remove('*')
                f=1
        print("The computer removed ", compballs, "from bag ", compbag)
        print("--------------------------------------------------------------\n")