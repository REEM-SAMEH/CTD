list=[]
while True:
    r = input("insert number: ") 
    if r == 'q':
        break
    else:
        list.append(r)
print("largest number is ", max(list))
print("smallest number is ",min(list))
