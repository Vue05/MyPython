print('''
,----.    ,-.   ,----.,------. ,-.   ,-.,-. ,-.
    / ,-,_/  ,'  |  / /"P /`-, ,-','  |  / //  |/ /
   / / __  ,' ,| | / ,---'  / / ,' ,| | / // J P /
  / '-' /,' ,--. |/ /      / /,' ,--. |/ // /|  /
  `----''--'   `-'`'.--""""--.--'   `-'`' `' `-'
  nnnnnnnnnnnnnnnn,'.n*""""*N.`.#######################
  NNNNNNNNNNNNNNN/ J',n*""*n.`L \##### ### ### ### ####
                : J J___/\___L L :#####################
  nnnnnnnnnnnnnn{ [{ `.    ,' }] }## ### ### ### ### ##
  NNNNNNNNNNNNNN: T T /,'`.\ T J :#####################
                 \ L,`*n,,n*',J /
  nnnnnnnnnnnnnnnn`. *n,,,,n* ,'nnnnnnnnnnnnnnnnnnnnnnn
  NNNNNNNNNNNNNNNNNN`-..__..-'NNNNNNNNNNNNNNNNNNNNNNNNN
  ,-.    ,-.  ,-. ,----. ,----.,-. ,----.   ,-. 
  |  `.  \  `.|  \\  .--`\ \"L \\ \\ .-._\  |  `. o!0
  | |. `. \ \ ` L \\  __\ \ .  < \ \\ \  __ | |. `.
  | .--. `.\ \`-'\ \\ `---.\ \L `.\ \\ `-` \| .--. `. 
  `-'   `--``'    `-'`----' `-'`-' `' `----'`-'   `--'
    ''')

print("Welcome to the avengers game!")
print("I'm Captain America, and i'm here to save you, all you need to do is find me")
print("You're in trouble. Who do you want to save you, superhuman or demigod?  ")
to_save = input("Type 'superhuman' or 'demigod'\n").lower()


if to_save == "superhuman":
    gender_to_save = input("Welcome to the avengers lair." \
        " Would you like a male or female hero? " \
        "Type 'M' for male, type 'F' for female: \n").lower()
    if gender_to_save == "m":
        male_hero = input("You have three options: 'Iron Man', 'Captain America' or 'Spiderman', choose your hero;\n").lower()
        if male_hero == "iron man":
            print("If only he could find time between being a genius, playboy, hero, philanthropist aaand billionaire, he'd actually come." \
                 " How cute of you though, ciao!")
        elif male_hero == "spiderman":
            print("Are you kidding?! He doesn't even remember MJ, his memory is webbed!")
        elif male_hero == "captain america":
            print("Took ya long enough! I'll save you citizen, for a small fee of a pack of glazed donuts. A 6 pack, get it?")
        else:
            print("You've reached the avenger voicemail. I'm currently on vacation in Wakanda, leave a message!")
    else:
        print("SERVICE UNAVAILABLE... The ladies are on a spa date")
        
else:
    print("Welp, Adios! Thor's having a squabble with Loki, per usual. You can wait till they're done. P.S. That's never!")


