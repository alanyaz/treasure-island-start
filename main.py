print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice_1= input('You are at a crossroad.where do you want to go?Type "Left"or "right". ').lower()

if choice_1=="left":
   choice_2=input("You have come to a lake. There is an island in the 
   middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to 
   swim across. ").lower()   
   if choice_2=="wait":
     choice_3=input("You arrive at the island unharmed. there is a 
     house with 3 doors. one red, one yellow and one blue. which 
     colour do you choose?").lower()  
     if choice_3=="red":
        print('It is a room full of fire game over')            
     elif choice_3="yellow":
          print('You found the treasure! You win')
     elif choice_3="blue":  
          print('You enter a room of beats. Game over')
     else:
          print(' You chose a door that does not exist Game ober!')   
                    
   else:
   print("you got attacked by an angry trout. Game over")       

else :
   print("You fell into a hole. Game Over")



