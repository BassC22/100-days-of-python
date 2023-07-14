print('''                        
              ___       
              \\||      
             ,'_,-\     
             ;'____\    
             || =\=|    
             ||  - |                               
         ,---'._--''-,,---------.--.----_,         
        / `-._- _--/,,|  ___,,--'--'._<            
       /-._,  `-.__;,,|'                           
      /   ;\      / , ;                            
     /  ,' | _ - ',/, ;
    (  (   |     /, ,,;
     \  \  |     ',,/,;
      \  \ |    /, / ,;
     (| ,^.|   / ,, ,/;
      `-'./ `-._,, ,/,;
           �-._ `-._,,;
      jrei |/,,`-._ `-.
           |, ,;, ,`-._\
''')
print()
print()
print("Welcome to Empire Battle.")
print("Your mission is to survive or defeat your enemy.\n")

ques1 = input("It's the dark ages, what do you do first?\nType 'house' to build a house or 'food' to forage for berries.\n").lower()
if ques1 == "house":
  ques2 = input("A snowstorm arrives and luckily you have set up your home in which you shelter.\nSuddenly, your village is being attacked by an invading enemy.\nType 'fight' to fight them off or 'hide' to go into hiding.\n").lower()
  if ques2 == "fight":
    print("Your enemy is armed with ballistics and your primitive club is no match, you are defeated!")
  if ques2 == "hide":
    ques3 = input("Your rudimentary weapons would have been no match against your enemy's ballistics, it's a good job you hid!\nEventually they leave and you can continue developing your empire. What's next on the to-do list?\nType 'medicine' to work on medicines, type 'farming' to work on stockpiling grain, type 'wood' to work on construction or type 'weapons' to develop ballistics.\n").lower()
    if ques3 == "medicine":
      print("A flesh-eating bug infects the whole city, but luckily you developed medicines to overcome it.\nYour enemies weren't quite so lucky and succumb to the disease.\nYou are victorious!")
    elif ques3 == "farming":
      print("All that grain attracts the village's vermin and they feast on your supplies.\nYou starve to death!")
    elif ques3 == "wood":
      print("Your village boasts a whole host of the latest timber buildings. However, a fire sweeps through the settlement and destroys everything.\nYou burn to death!")
    elif ques3 == "weapons":
      print("You decide to arm yourself against your enemies and work on the latest ballistic weapons.\nSadly, some straw catches fire in the workshop, causing all the weapons to explode and rendering you defenseless against attack.\nYou are defeated!")
if ques1 == "food":
  print("A snowstorm arrives and you have nowhere to shelter, you freeze to death!")
  
