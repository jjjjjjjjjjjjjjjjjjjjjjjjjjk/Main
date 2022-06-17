print("Welcome to the 🧨 store\n\n\n")
bomb = input("Would you like a bomb? ") 
if bomb == "yes":
  print("here are the Options:\n\n")
  menu = input("Which one would you like? C4, Bath-Bomb, Land-Mine, Or Bunker-Blaster?\n")
  Confirm = input(menu + ",is this correct?\n")
  if Confirm == "yes":
    print("Okay!")
  else: exit()
  
k = input("Order now? ")
if k == "yes": 
  print("okay! Ordered")
else: exit()
  
print("one more question whats your address?")
address = input("")
print(address) 
unit = input("is this correct? ")
if unit == "yes":
    print("Okay order should arive to, " + address + " in 2 weeks.")
else: exit()
