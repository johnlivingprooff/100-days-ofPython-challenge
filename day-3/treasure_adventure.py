#!/usr/bin/python3

print('''

██   ██▄       ▄   ▄███▄      ▄     ▄▄▄▄▀ ▄   █▄▄▄▄ ▄███▄   
█ █  █  █       █  █▀   ▀      █ ▀▀▀ █     █  █  ▄▀ █▀   ▀  
█▄▄█ █   █ █     █ ██▄▄    ██   █    █  █   █ █▀▀▌  ██▄▄    
█  █ █  █   █    █ █▄   ▄▀ █ █  █   █   █   █ █  █  █▄   ▄▀ 
   █ ███▀    █  █  ▀███▀   █  █ █  ▀    █▄ ▄█   █   ▀███▀   
  █           █▐           █   ██        ▀▀▀   ▀            
 ▀            ▐                                             
          
''')

# The Code
print("Welcome to Adventures ϐ")
ans = input("Would you like to proceed? [Yes/No] ")
ans = ans.lower()
if ans == "yes":
   print("Let the Games, begin..")
   print('''
Storyline:
In the Kingdom of Eldoria, a land steeped in magic and mystery, a powerful artifact known as the Crystal of Eternity has been stolen.\nThis crystal, which holds the balance of magic in the realm, is said to have the ability to grant unimaginable power to anyone who possesses it.\n\nIts theft has thrown Eldoria into chaos, with magical disturbances and dark shadows spreading across the land.
            ''')
   player = input("Choose your character -> [Villager | Temple Priest] ")
   player = player.lower()
   if player == "villager":
        print("You encounter a vision from the Oracle")
        part_one = (input("Speak to the priest, or keep quiet [Speak/Be quiet] ")).lower()
        if part_one == "speak":
            print("You discover from your conversation, and acute discernment, that something's fishy about the priest")
            part_two = (input("Report to the council of Elders or become a solo detective\
                              \nChoose your path [Detective / Reporter]")).lower()
            if part_two == "reporter":
               print("The priest discovers your plot to uncover his dirty secrets to the council, and he detains you!")
               print('''

  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
█ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
█   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
 ███     █    █  ▀███▀               █  █  ▀███▀     █   
        █    ▀                        █▐            ▀    
       ▀                              ▐                  

                        ''')
            elif part_two == "detective":
                  print("You're faced with a dilemma, you can't take on the priest alone")
                  print("You need allies")
                  ally = (input("Who among the potential allies do you choose to recruit first: the mage, the rogue, or the warrior? ")).lower()
                  if ally == "rogue":
                        print("he snitches on you, it's over")
                        print('''

  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
█ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
█   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
 ███     █    █  ▀███▀               █  █  ▀███▀     █   
        █    ▀                        █▐            ▀    
       ▀                              ▐                  

                        ''')
                  elif ally == "warrior":
                        print("You are victorious in your quest!")
                        print('''

_____._.___.__  ._______     ._______.______  .______  
\__ _:|:   |  \ : .____/     : .____/:      \ :_ _   \ 
  |  :||   :   || : _/\      | : _/\ |       ||   |   |
  |   ||   .   ||   /  \     |   /  \|   |   || . |   |
  |   ||___|   ||_.: __/     |_.: __/|___|   ||. ____/ 
  |___|    |___|   :/           :/       |___| :/      
                                               :       
                                                       
                                                       

                                 ''')
                  else:
                        print(f"Love your choice of {ally}, sometimes it's good to think outside the box ^_^")
                        print('''

  '  |)¯¯)¸.·´¨¯¯(| °       '|)¯¯)          *     |\¯¯\      '|\¯¯\    °          '|)¯¯)¸.·´¨¯¯(|‚‚    '  |\¯¯\`·.¯`·.   
  .·´  .·´)_____'`·.„    .·´' .·´(¯¯(|    _     '| ;   ';     '|';   ';‘            .·´  .·´)_____'`·.°    '| ;   '; '|\   '\  
(    (¸.·´_(|         |   '(   '(|__|'·. '`·.‚         /   '/|°     /   '/|‘         *(    (¸.·´_(|        '|‚’     '/   '/|*'|/   '/| 
'|`·. '`·.'   |____  '|    |)   ')¯¯¯|)   ')     .·´ '.·´|*|°   '/   '/¸.·´¨¯(|'   *'|`·.  `·.¸.·´¨¯¯¯.·´|   .·´' .·´|'.·´' .·´| |‚
'|  '|)__)_'|        °  '.·´_.·´|   .·´_.·´|°  '(__(|_ |/°  '*|\__.·´)___'·.º_|  '|)__.·|¨)__(|   '| '(__(|.·´_.·´  *'|/‚‚
 `·.|    |’              |    | *'|¯ |    |  '|°   |    |.·´     _| |  |  '|        |   `·.|    | '|'|     | .·´‚  |   '||    '|'   .·´   
    |__'|‚              |__'|.·´ * |__'|.·´‚‚   |__'|          '\|_|.·'|____*|      |__'|.·'|___|‚      |__||__ |.·´     ‚‚

                                 ''')
        elif part_one == "be quiet":
               print('''

    '        ‘             ‘         '          °                 ___°             ___             ____‚    
        ____°        ____ ‚   ’ ‚               ___    /¯¯¯/|__„   ___|\¯¯¯\     ___|\¯¯¯¯\‚  
  ___|\¯¯¯\       /¯¯¯¯/|___°   ___     |\¯¯¯\ '/    ' /\¯¯¯\°|¯¯¯¯|\     \‚  |¯¯¯¯|\       \°
'/¯¯¯¯/\___\‚‚  '/       /'\¯¯¯¯\°|¯¯¯|  _ \|    ' |‘|    ' |_|  '   |‚|       |/     /|  |       |:|       |‚
|       |'\|'¯'  '|_‚ |       |::|      ' |‚|\     \/¯\/     /| |  '   |¯|'     |‚|;;:    |\     \|  |       |:|:;   ;;|‚
|\____\/¯¯¯¯/|‚|\____\/       /|‚'\ \___/\___/'/‘ |'     |¯|    ' |‚|____|\'\     \°|____|/      '/|„
'\|'¯' '¯/____/;/”'\|'¯' '¯/____/'/‚‚  \|'¯' '|/\|'¯' |/‘'  |\___\'| '°   |‚|'¯ ¯ |  \|___|”|'¯' ¯'/____/'/‚‚
   ¯¯¯|'¯' ¯ |/     '¯¯¯|'¯' ¯¯|/‚      ¯¯    ¯¯'  ‚  '\|'¯'  |/___/|‚ ¯¯¯     |'¯'¯|  ¯¯¯|'¯' ¯¯|/’  
         ¯¯¯¯°           ¯¯¯¯”   °      °                ¯¯|'¯'  ¯|/”            ¯¯¯        ¯¯¯¯’    
    '        ‘             ‘         '                    °           ¯¯¯°         '  ‘                ‘          

                     ''')
        else:
               print(f"Your choice {part_one} is rejected It's GameOver for you!")

   elif player == "temple priest":
       print(f"the {player} is a fraud -> Gameover!")
         
   else:
        print("No adventure for you, except you're a villager")
elif ans == "no":
    print("Until next time!\nGoodbye ^_^")
else:
    print("We always love someone who thinks outside the box!")
    print("But you can't proceed")
