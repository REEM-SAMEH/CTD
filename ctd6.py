
import random
import cv2

rows, cols = (3, 10)
bags=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append('O')
    bags.append(col)

def onGame(): # Checks all bags not Empty
  for i in range (3):
    if len(bags[i]) != 0:
      return True
  return False

def check_bag(n): # Check index
  if n > 3 or n < 1:
    print("Enter Bag Between 1 - 3 !")
    return False  
 
  if len(bags[n-1]) == 0: # Check Empty Bag
    print(f"bag {n} is Empty")
    return False
  # Valid Bag input
  return True

def check_balls(n, x):
  if n > 5 or n < 1:
    print("Enter Balls Between 1 - 5 !")
    return False 
  if n > len(bags[x]):
    print (f'you entered {n} which is Bigger than what in bag {x}')
    return False
  # Valid to remove balls
  print(f'You removed {n} from bag {x+1}')
  for i in range(n):
    del bags[x][0]
  return True
  
def UserInput(): #user
  # Bag input
  try:
    bag_n = int(input("Number of Bag (1 - 3): "))
    check = check_bag(bag_n)
    if check is False:
      return False
  except ValueError:
    print("Enter Number between 1 - 3")
    
  # Balls input
  valid = False
  while valid is False:
    try:
      balls = int(input("Number of Balls (1 - 5): "))
      valid = check_balls(balls, bag_n-1)
    except ValueError:
      print("Enter Number between 1 - 5")

  # bag & balls input is OK
  return True
    
def computerTurn():
    # rand until get valid number
  while True:
    rowComp  = random.randint(0,2)
    if len(bags[rowComp]) != 0:
      break
  while True:
     colComp = random.randint(1,5)
     if colComp <= len(bags[rowComp]):
       break;
  print(f'computer removed {colComp} from bag {rowComp + 1}')
  for i in range(colComp):
    del bags[rowComp][0]

userwin = False
# Game Loop
while onGame():
  # print bags
  for bag in bags:
    print(bag)
    
  if UserInput() is True:   # User Turn
    for bag in bags:
      print(bag)
    if onGame() is False:
      userwin = True
      break
    computerTurn()
    print ('-------------------------------------------------------\n')
    
if userwin: #picture opencv lib
  img = cv2.imread(r"D:/roben/win.jpg")
  cv2.imshow("You WIN", img)
else:
  img = cv2.imread(r"D:/roben/losee.jpg ")
  cv2.imshow("You Lost", img)

cv2.waitKey(0)  
cv2.destroyAllWindows()
