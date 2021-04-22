




def run_main():

    hero_name = "sadid"
    hero_live = 300

    villain_name = "reham"
    villain_life = 250

    buddy_one_name = "nafiz"
    buddy_one_life = 100

    buddy_two_name = "fara"
    buddy_two_life = 100

    heroine_name = "shihab"
    heroine_released = False

    fight_cycles = 0

    while(heroine_released == False):

        fight_cycles = fight_cycles + 1

        if(fight_cycles%5==0):
            buddy_one_life = fire_shotgun(villain_name,villain_life, buddy_one_name, buddy_one_life)
            buddy_two_life = fire_shotgun(villain_name, villain_life, buddy_two_name, buddy_two_life)

        else:
            villain_life = mele_attack(buddy_one_name, buddy_one_life, villain_name, villain_life)
            villain_life = mele_attack(buddy_two_name, buddy_two_life, villain_name, villain_life)
            villain_life = ninja_move(hero_name,hero_live, villain_name, villain_life)
            villain_life = ninja_move(hero_name, hero_live, villain_name, villain_life)
            hero_live = choke_slam(villain_name, villain_life, hero_name, hero_live)

        heroine_released = check_if_lady_is_secured(villain_life, villain_name)



def mele_attack(from_name, from_life, to_name, to_life):

    if from_life < 5:
        print(from_name + " says : " + "Listening Pink Floyed in heaven!")

    else:
        to_life = to_life - 5
        if(to_life < 1):
            print("\n\n"+from_name + " says : Mama just killed " + to_name)
        else:
            print(from_name + " says : Mele Attaaaaack! Screw you " + to_name )

    return to_life

def ninja_move(from_name, from_life, to_name, to_life):

    if from_life < 1:
        print(from_name + " says : " + "Listening Pink Floyed in heaven!")

    else:
        to_life = to_life - 15
        if(to_life < 1):
            print("\n\n"+from_name + " says : Mama just killed " + to_name)
        else:
            print(from_name + " says : Take that ninja move! Screw you " + to_name )

    return to_life

def choke_slam(from_name, from_life, to_name, to_life):

    if from_life < 1:
        print(from_name + " says : " + "Listening Pink Floyed in heaven!")

    else:
        to_life = to_life - 20
        if(to_life < 1):
            print("\n\n"+from_name + " says : Mama just killed " + to_name)
        else:
            print(from_name + " says : Em gonna Choke Slam you scar face! Screw you " + to_name )

    return to_life


def fire_shotgun(from_name, from_life, to_name, to_life):
    if from_life < 1:
        print(from_name + " says : " + "Listening Pink Floyed in heaven!")

    else:
        to_life = to_life - 80
        if (to_life < 1):
            print("\n\n" + from_name + " says : Mama just killed " + to_name)
        else:
            print("\n" + from_name + " says : Boom Boom Gunpowder Rules! Screw you " + to_name + "\n")

    return to_life

def check_if_lady_is_secured(villain_life, villain_name):

    if(villain_life < 1):
        print("\n\n" + villain_name + " is dead. Love is secured. Peace on earth!")
        return True

    else:
        return  False




run_main()


