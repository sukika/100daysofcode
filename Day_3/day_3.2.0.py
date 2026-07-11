sunsetart =  r""" 
........::::::::::::..           .......|...............::::::::........
     .:::::;;;;;;;;;;;:::::.... .     \   | ../....::::;;;;:::::.......
         .       ...........   / \\_   \  |  /     ......  .     ........./\
...:::../\\_  ......     ..._/'   \\\_  \###/   /\_    .../ \_.......   _//
.::::./   \\\ _   .../\    /'      \\\\#######//   \/\   //   \_   ....////
    _/      \\\\   _/ \\\ /  x       \\\\###////      \////     \__  _/////
  ./   x       \\\/     \/ x X           \//////                   \/////
 /     XxX     \\/         XxX X                                    ////   x
-----XxX-------------|-------XxX-----------*--------|---*-----|------------X--
       X        _X      *    X      **         **             x   **    *  X
      _X                    _X           x                *          x     X_
"""
print(sunsetart)

print("Welcome to Sunset Island")
print("Your being chased by Caseoh make sure to make it out alive!")

answer = input("Caseoh is already chasing you, do you accept your fate or run? Yes Or No? ").lower()
    
if answer == "no":
    print("You've been eaten by caseoh")
elif answer == "yes":
    print("You better hurry and start picking up the pace!!!") 
    crossroads = input ("Your at the crossroads where do you turn, right or left? ")
    if crossroads == "left":
         print("Gameover. At the crossroads, don't turn left")
    elif crossroads == "right":
        print("Your now at the mountain")
        mountain = input("As Caseoh trips, causing rocks to fall. There is a small cabin do you hide to take cover, yes or no? ")
        if mountain == "no":
             print("Gameover. You've been caught in all the rocks and caseoh manages to eat you!!!")
        elif mountain == "yes":
              print("Forunately you are saved from the rocks falling on you")
              cabin = input("Caseoh, manages to find you in the cabin do you plea with him yes or no? ")
              if cabin == "no":
                   print("Gameover. Caseoh eats you.")
              elif cabin == "yes":
                   print("Caseoh stops to hear you speak.")
                   plea = input("As you plea with Caseoh, you realize Caseoh is hungry where do you take him? Tacobell , Mcdonalds , and Arbys? ")
                   if plea == "Tacobell":
                       print("Gameover. Caseoh has beef with tacobell as it gave him food poisoning so he ate you instead.")
                   elif plea == "Arnys":
                        print("Caseoh tears you apart and eats you.")
                   elif plea == "Mcdonalds":
                         print("Caseoh is very pleased with you choice")
                         print("Chapter 2")
                         salad = input("Although Caseoh was satistfied with his meal at Mcdonalds, he is still wants to eat you what do you do? Take him to a salad bar, play dead by daylight, or take him to sonic? ")    
                         if  salad == "play dead by daylight":
                          print("Gameover. Caseoh gets so mad he jumps again which causes in earthquake and kills you.")
                         elif salad == "take him to a salad bar":
                          print("Better than the other options")
                         elif salad == "sonic":
                              print("Better than the other options.")
                              sonic = input("Your at sonic with Caseoh what do you order? twofoot long hot dogs, premium chicken bites, and cheese burger? ")
                              if sonic == "premium chicken bites":
                                        print("Gameover. Caseoh eats you.")
                              elif sonic == "two foot long hot dogs":
                                        print("Good choice, Caseoh is very pleased")
                                        fries = input("The server asks you if you would like some fries yes or no? ")
                                        if fries == "yes":
                                             print("Gameover. Caseoh is so mad at you as he hates sonic fries and eats you.")
                                        elif fries == "no":
                                             print("Caseoh is pleased that your remember he hates sonic fries")
                                             still = input ("Caseoh is still hungry, where should you take him now? Freddys, Wendys, Canes? ")
                                             if still == "Freddys":
                                                  print("Gameover. Caseoh doesn't want Freddys")
                                             elif still == "Wendys":
                                                  print("Good choice, Caseoh is happy.")
                                                  wendy = input ("Your at the drive thru what should you order? Spicy Nuggets, Triple Baconator, Small fries ")
                                                  if wendy == "Triple Baconator":
                                                       print("Gameover. Caseoh is not pleased.")
                                                       print("Chapter 3")
                                                  elif wendy == "Spicy Nuggets":
                                                       print("Caseoh is so happy he did a backflip")               
                                                       backflip = input ("After Caseoh did a backflip now there is tsunami warnings in the area should you get gas? yes or no? ")
                                                       if backflip == "no":
                                                            print("Gameover. You ran out of gas and the tsunami consumed you.")
                                                       elif backflip == "yes":
                                                            print("Good your are very low and gas and wouldn't have made it without gas.")
                                                            gas = input ("Your at the gas station, which type of gas should you get disel or gas? ")
                                                            if gas == "disel":
                                                                 print("Gameover. Wasn't the right gas type and you died since the car couldn't run.")
                                                            elif gas == "gas":
                                                                 print("Good thinking your car can't do disel!")
                                                                 station = input("You and Caseoh decide to go into the gas station for some supplies, what should you get life jacket, swim goggles, or pizza ")
                                                                 if station == "swim goggles":
                                                                  print("Gameover. The swim goggles weren't much help")
                                                                 elif station == "life jacket":
                                                                      print("At least you know some basic needs")
                                                                      help = input("As you leave the store, Tung Tung Sahur asks if you would like some extra gas canisters for $6.7. Do you accept yes or no? ")
                                                                      if help == "yes":
                                                                           print("You ended up needing those canisters in the end")
                                                                      elif help == "no":
                                                                           print("Gameover. you needed those as you ran out of more gas")
                                                                           tung = input("Tung Tung Sahur is wondering if he could join you and Caseoh to escape the tsunami. Do you accept him yes or no? ")
                                                                           if tung == "no":
                                                                                print("Game Over. In the end you needed Tung Tung Sahur to save you.")
                                                                           elif tung == "yes":
                                                                                print("Good, you needed him.")
                                                                                print("Chapter 4")
                                                                                road = input("As you leave the gas station you wonder which road you should take, sunset or island road")
                                                                                if road == "island road":
                                                                                     print("Game Over. Bro your cooked.")
                                                                                elif road == "sunset":
                                                                                     print("Perfect your on the right track!")
                                                                                     radio = input("Tung Tung Sahur reccomends you turn on the radio to see when the tsunami is coming, do you turn on the radio yes or no?")
                                                                                     if radio == "no":
                                                                                               print("Game Over. Did you get your survival skills from a cow?")
                                                                                     elif radio == "yes":
                                                                                               print("Good survival instincts!")
                                                                                               highway = input("The highway is absolute chaos do you stay on the highway or take a back road? stay or take the back road ")
                                                                                               if highway == "stay":
                                                                                                    print("Game Over. Buddy you ain't going no where on that highway")
                                                                                               elif highway == "take the back road":
                                                                                                     print("Good thinking!")
                                                                                                     traffic = input ("The tsunami according to the radio is getting closer but you keep hititng every red light Caseoh says to break the law. Do you choose to be a law abiding citizen yes or no? ")
                                                                                                     if traffic == "yes":
                                                                                                         print("Game Over. Are you crazy there was no one on the road?")
                                                                                                     elif traffic == "no":
                                                                                                         print("fast and furious")
                                                                                                         gps = input ("You can't find a hotel anywhere which gps should you use google or apple maps? ")
                                                                                                         if gps == "apple":
                                                                                                              print("Game Over. BUDDY APPLE MAPS AINT GONNA SAVE YOU NOWW")
                                                                                                         elif gps == "google":
                                                                                                              print("Better choice than apple, but the google voice does drive you insane.")
                                                                                                              print("Chapter 5")
                                                                                                              hotel = input ("Your trying to find the tallest hotel in your area but don't know which hotel to decide on its either the Marriot or Hiliton? ")
                                                                                                              if hotel == "Hilition":
                                                                                                                   print("Game Over. Your cooked.")
                                                                                                              elif hotel == "Marriot":
                                                                                                                    print("Good choice")
                                                                                                                    stair = input ("You've arrived at the hotel but what do you take the elevator or the stairs")
                                                                                                                    if stair == "elevator":
                                                                                                                             print("Game Over. Your survival instincts are horrible")
                                                                                                                    elif stair == "stairs":
                                                                                                                        print("Now were talking!")
                                                                                                                        passage = input ("Caseoh finds a kitchen that you can cut through to do you take it? yes or no? ")
                                                                                                                        if passage == "yes":
                                                                                                                             print("Game Over. Forgot you needed to get on top of the roof and just stuffed your mouth with food.")
                                                                                                                        elif passage == "no":
                                                                                                                             print("Smart thinking!")
                                                                                                                             roof = input("You get to the roof top but theres no tsunami, what do you do? Wait it out or Leave? ")
                                                                                                                             if roof == "leave":
                                                                                                                                  print("Game Over. The tsunami still came")
                                                                                                                             elif roof == "Wait it out":
                                                                                                                                  print("Good you waitied it out as the tsunami still came!")     
                                                                                                                                  hungry = input ("Your very hungry do you decided to eat yes or no? ")     
                                                                                                                                  if hungry == "no":
                                                                                                                                       print("Game Over. You died from hungry")
                                                                                                                                  elif hungry == "yes": 
                                                                                                                                       print("You head to McDonalds again and have the best meal of your life")
                                                                                                                                       print("The end good job you managed to survived!!")
                                                       else:
                                                            print("Game Over. Caseoh ate you.")