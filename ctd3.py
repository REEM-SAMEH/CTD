bag=[5,9,1,7,3,19]
while True :
    print(bag)
    if(len(bag)>4):
        x=str(input("remove or enter : "))
        y=int(input("enter number : "))
        if(x=='remove'):
            bag.remove(y)
        elif(x=='enter'):
            bag.append(y)
    else:
        print("cannot remove, bag is at minimum capacity")
        print(bag)
        x=str(input("enter only available : "))
        y=int(input("enter number : "))
        if(x=='enter'):
            bag.append(y)