#Final test day 3
import os
import time

def loading():         #function to call the fake loading
    os.system('cls')
    time.sleep(0.2)
    print("L")
    time.sleep(0.2)
    print("o")
    time.sleep(0.2)
    print("a")
    time.sleep(0.2)
    print("d")
    time.sleep(0.2)
    print("i")
    time.sleep(0.2)
    print("n")
    time.sleep(0.2)
    print("g")
    time.sleep(0.8)
    os.system('cls')
    time.sleep(0.2)
    print("L")
    time.sleep(0.2)
    print("o")
    time.sleep(0.2)
    print("a")
    time.sleep(0.2)
    print("d")
    time.sleep(0.2)
    print("i")
    time.sleep(0.2)
    print("n")
    time.sleep(0.2)
    print("g")
    time.sleep(0.8)
    os.system('cls')

def game_over(): 
   gameover = input('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼''')

victim = input("What's your name?")

os.system('cls')

print(f"Sup {victim}, Welcome to the... OMG LOOK AT THAT RHINO COMING AT YOU! FAST DO SOMETHING!!!")

time.sleep(2)

print('''       ,       ,
      /|    |\./'.
     | |  ,  \|| ,|
     \  \_(\.-""\//.  _
   .-'`""``"` _   ` `-.`"""--.._      _..----. __
   | '~`      o\                `"---"        `. `"-.==,
    \,.-;    `"`                                |`""`===`
      (`            /                           |               }* / "* / "*
       `-----.____.;          \     |           ;
                   \__         |    \          /                       }* / "* / "*
                  .'         .'      \        ' `,
                 /          /         '._        |         }* / "* / "*
                 |    '.---;`-.____.-'`\ `""`;   |
                 |     _\   \    '.     )   /   "\"                  }* / "* / "*
                 \-,--( /   /    _/   .'   |_ _ .-)         }* / "* / "*
                  '----;)__;    (`.-. ;    `-:.;-'
                                 `""""`'''
)
time.sleep(1)
c1 = input("Type one of the numbers:\n1: Pray.\n2: Try to use your charisma and argue with the beast.\n3: Just run away.\n4: Fake death.\n")

loading()
if c1 == "1":
    
    print( '''               .    .
                |\   |"\"
             _..;|;__;|;
           ,'   ';` \';`-.
           7;-..     :   ) 
      .--._)|   `;==,|,=='
       `\`@; \_ `<`O," O).
         `\/-;,(  )  .>. )     The Rhino didn't care for your Gods and just stampede you with no mercy. 
             < ,-;'-.__.;'               Will be hard to clean your remais from the floor...
              `\_ `-,__,'
                 `-..,;,>
                    `;;;;
                     `  `''')
if c1 == "2":
    
    print( '''               .    .
                |\   |"\"
             _..;|;__;|;
           ,'   ';` \';`-.
           7;-..     :   ) 
      .--._)|   `;==,|,=='
       `\`@; \_ `<`O," O).
         `\/-;,(  )  .>. )     The Rhino didn't got your good manners and just stampede you with no mercy. 
             < ,-;'-.__.;'               Will be hard to clean your remais from the floor...
              `\_ `-,__,'
                 `-..,;,>
                    `;;;;
                     `  `''')
if c1 == "3":
    
    print( '''               .    .
                |\   |"\"
             _..;|;__;|;
           ,'   ';` \';`-.
           7;-..     :   ) 
      .--._)|   `;==,|,=='
       `\`@; \_ `<`O," O).
         `\/-;,(  )  .>. )     You seriously tough that you can outrun a rhino??? 
             < ,-;'-.__.;'               Will be hard to clean your remais from the floor...
              `\_ `-,__,'
                 `-..,;,>
                    `;;;;
                     `  `''')
if c1 == "4":
    
    print( '''               .    .
                |\   |"\"
             _..;|;__;|;
           ,'   ';` \';`-.
           7;-..     :   ) 
      .--._)|   `;==,|,=='
       `\`@; \_ `<`O," O).
         `\/-;,(  )  .>. )       Don't worry, you don't need to fake it anymore. 
             < ,-;'-.__.;'               Will be hard to clean your remais from the floor...
              `\_ `-,__,'
                 `-..,;,>
                    `;;;;
                     `  `''')
    

c2 = (input(f"Did you like the game, {victim}?\nType Y or N: "))
c2 = c2.lower()

if c2 == "y":
   os.system('cls')
   time.sleep(0.2)
   print("L")
   time.sleep(0.2)
   print("o")
   time.sleep(0.2)
   print("a")
   time.sleep(0.2)
   print("d")
   time.sleep(0.2)
   os.system('cls')
   print(f"Ohh, you are so kind {victim}! Because of that I can let you continue your story.")

if c2 == "n":
   os.system('cls')
   time.sleep(0.2)
   print("L")
   time.sleep(0.2)
   print("o")
   time.sleep(0.2)
   print("a")
   time.sleep(0.2)
   print("d")
   time.sleep(0.2)
   os.system('cls')
   print(f"You think it's easy to tolerate you, {victim}? Because of that I will continue your misery. Ops, story.\n")


print("So, you realise that it was all a bad dream. Now it's all good, you have awoken... in a cold stone floor.\nYou are in a small tomb, the only things that you see is spiders and a metal gate opened.")
time.sleep(3)

print('''
_________+______/      \______+__________
  __--   |       R.I.P.       |-_-- __
_-- -    | ___ __________ ___ |
-_-- __  || | | | {|    /| | || __---  -_
 --__-   || | | | {|   /|| | ||--        -
         || | | | {|  /||| | ||__--
 __-- -__|| | | | {| |}||| | ||--   __--
         ||_|_|_|_{| |}|||_|_||  -__
 --__-  -|| | | | {& |}||/ | ||---   __--
         || | | | {| |}|/| | ||-__
--   __--|| | | | {| |}/|| | ||__-- -__
  --     || | | | {| &}||| | ||   __
---   __-|| | | | {| |}||| | ||_---__-  --
 -  -_   || | | | {| |}||| | || --
 __ejm 97|| | | | {| |}||| | ||_--__-   _---
_________||_|_|_|_{| |}|||_|_||______________
                     |}|/
                     |}/
                     |/''')

time.sleep(2)

c3 = (input(f"What you do?\n1: CLose the gate and stay inside.\n2: Leave the tomb."))

if c3 == "1":
   os.system('cls')
   time.sleep(0.2)
   print("L")
   time.sleep(0.2)
   print("o")
   time.sleep(0.2)
   print("a")
   time.sleep(0.2)
   print("d")
   time.sleep(0.2)
   os.system('cls')
   print(f"Well, nothing happened {victim}... After a long bored time you decide to leave, anyway the spiders was friggtening you.")

if c3 == "2":
   os.system('cls')
   time.sleep(0.2)
   print("L")
   time.sleep(0.2)
   print("o")
   time.sleep(0.2)
   print("a")
   time.sleep(0.2)
   print("d")
   time.sleep(0.2)
   os.system('cls')
   print(f"When you put your foot outside, you see a living skelleton.")

time.sleep(2)
print('''
                                                  /)_("\"
                                           ______( 0 0 )______
                                          /_/_/_/\` ' `/\_\_\_"\"
                                                  )'_'(
                                             ____.""_"".____
                                            |___|___|___|___|
                                              |___|___|___|
         Damn! why am I always                  |-      |
  forget where i put my right arm?...           |       |
                        /                      _|_______|_
                    ___                       |___|___|___|
                   /   \                        |'   | ||
                   )'__/                        |       |
                   \(\\                         |       |
                     _\\__                      |       |
                    /,_ \-                      |     - |
               ____// \ |                       |       |
              /,-' `  _)/                       |       |
              ``     ,o_:)                      |       |
         .          /    \        .             |       |
                   /      \                     | |     |
      .    (      c        c     )    .         |       |
       (    )      \      /     (    )          |       |
      ( )  '        |     |      '  ( )        _|_______|_
      _#, .    ...,:o    o:,..    . ,#_ ,, ,,,|___________|,,,
''')
c4 = input("You try to:\n1: sneak pass it.\n2: Say hello?")

if c4 == "1":
   os.system('cls')
   time.sleep(0.2)
   print("L")
   time.sleep(0.2)
   print("o")
   time.sleep(0.2)
   print("a")
   time.sleep(0.2)
   print("d")
   time.sleep(0.2)
   print("i")
   time.sleep(0.2)
   print("n")
   time.sleep(0.2)
   print("g")
   time.sleep(0.2)
   os.system('cls')
   print(f"The skeleton didn't notice you, but now there's nowhere to go now, the cemetary is full of monsters that killed you. Slowly...")
   game_over()


if c4 == "2":
   os.system('cls')
   time.sleep(0.2)
   print("L")
   time.sleep(0.2)
   print("o")
   time.sleep(0.2)
   print("a")
   time.sleep(0.2)
   print("d")
   time.sleep(0.2)
   print("i")
   time.sleep(0.2)
   print("n")
   time.sleep(0.2)
   print("g")
   time.sleep(0.2)
   os.system('cls')
   print(f"The skeleton friendly ask how you doing. And explain to you that he need his arm.")

c5 = input("1: Tell him to stay away.\n2: Say that you gonna help.")
if c5 == "1":
   os.system('cls')
   time.sleep(0.2)
   print("L")
   time.sleep(0.2)
   print("o")
   time.sleep(0.2)
   print("a")
   time.sleep(0.2)
   print("He appear to be confused by your bad manner, he just ignores you and keep searching his arm.\nNow there's nowhere to go now, the cemetary is full of monsters that killed you. Slowly...")
   game_over()

if c5 == "2":
   os.system('cls')

   print("You two go together as a team in the quest for his arm. You never found his arm, but you made good friends in the cemetary because\nGreg, the skelleton knows everyone.")

   print('''  
                                ,-~-.
               ,_.,             >    :
              /   \%~,          i~,* ;
              \0 0/   "q        ""/ r
               |"|    //       __}={_.
             __.T._  //      .p}'}={`{q
          .p}---V--{d'      //---}={--'
          !\ ---I---       // ---}={--
           \\ --^--       //   --}={-
            `b====%'%====d'  3%==}={
               }={               }={
             (`~=~')           (`~=~')
             p(o_o)             P}V{l
             \\~^~|             || //
              \\ ||             ||//
               \\||             ||/
                \\|            /||
                 })           ({||
                //|           ||(l
               //||           || \\
              // ||           ||  \\
             pf  d|           ||   \\
            (X\  {Xy,        ,|b    \\
             `\\    ``     ""~XX)    Yb
               ``                      ''')
print(f"The monsters love to dance and you lived a good life until and after your death. Everyone likes you {victim}!")
time.sleep(14)
loading()
print('''
__| |___________________________________________________________________________| |__
__   ___________________________________________________________________________   __
  | |                                                                           | |  
  | |  ___    ___ ________  ___  ___          ________  ___  ________           | |  
  | | |\  \  /  /|\   __  \|\  \|\  \        |\   ___ \|\  \|\   ___ \          | |  
  | | \ \  \/  / | \  \|\  \ \  \\\  \       \ \  \_|\ \ \  \ \  \_|\ \         | |  
  | |  \ \    / / \ \  \\\  \ \  \\\  \       \ \  \ \\ \ \  \ \  \ \\ \        | |  
  | |   \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \_\\ \ \  \ \  \_\\ \       | |  
  | | __/  / /      \ \_______\ \_______\       \ \_______\ \__\ \_______\      | |  
  | ||\___/ /        \|_______|\|_______|        \|_______|\|__|\|_______|      | |  
  | |\|___|/                                                                    | |  
  | |                                                                           | |  
  | |                                                                           | |  
  | | ___  _________  ___            _________  ___  ___     ___    ___         | |  
  | ||\  \|\___   ___\\  \          |\___   ___\\  \|\  \   |\  \  /  /|        | |  
  | |\ \  \|___ \  \_\ \  \         \|___ \  \_\ \  \\\  \  \ \  \/  / /        | |  
  | | \ \  \   \ \  \ \ \  \             \ \  \ \ \   __  \  \ \    / /         | |  
  | |  \ \  \   \ \  \ \ \__\             \ \  \ \ \  \ \  \  /     \/          | |  
  | |   \ \__\   \ \__\ \|__|              \ \__\ \ \__\ \__\/  /\   \          | |  
  | |    \|__|    \|__|     ___             \|__|  \|__|\|__/__/ /\ __\         | |  
  | |                      |\__\                            |__|/ \|__|         | |  
  | |                      \|__|                                                | |  
  | |                                                                           | |  
  | | ________ ________  ________                                               | |  
  | ||\  _____\\   __  \|\   __  \                                              | |  
  | |\ \  \__/\ \  \|\  \ \  \|\  \                                             | |  
  | | \ \   __\\ \  \\\  \ \   _  _\                                            | |  
  | |  \ \  \_| \ \  \\\  \ \  \\  \|                                           | |  
  | |   \ \__\   \ \_______\ \__\\ _\                                           | |  
  | |    \|__|    \|_______|\|__|\|__|                                          | |  
  | |                                                                           | |  
  | |                                                                           | |  
  | |                                                                           | |  
  | | ________  ___       ________      ___    ___ ___  ________   ________     | |  
  | ||\   __  \|\  \     |\   __  \    |\  \  /  /|\  \|\   ___  \|\   ____\    | |  
  | |\ \  \|\  \ \  \    \ \  \|\  \   \ \  \/  / | \  \ \  \\ \  \ \  \___|    | |  
  | | \ \   ____\ \  \    \ \   __  \   \ \    / / \ \  \ \  \\ \  \ \  \  ___  | |  
  | |  \ \  \___|\ \  \____\ \  \ \  \   \/  /  /   \ \  \ \  \\ \  \ \  \|\  \ | |  
  | |   \ \__\    \ \_______\ \__\ \__\__/  / /      \ \__\ \__\\ \__\ \_______\| |  
  | |    \|__|     \|_______|\|__|\|__|\___/ /        \|__|\|__| \|__|\|_______|| |  
  | |                                 \|___|/                                   | |  
__| |___________________________________________________________________________| |__
__   ___________________________________________________________________________   __
  | |                                                                           | |  ''')