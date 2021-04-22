from User_Class import user
from Hero_Class import Hero
from Villain_Class import Villain
from Buddy_Class import Buddy
from Lady_Class import Lady


riham = Villain("riham","BME-4")
sadid = Hero("Sadid", "BME-4")
shihab = Lady("Shihab","BME-4")
nafiz = Buddy("Nafiz", "BME-4")
fara = Buddy("Fara", "BME-4")

track_dict = dict()
fight_cycle = 0




while(shihab.release_condition == False):
    fight_cycle = fight_cycle + 1


    riham.gun_fire(nafiz)
    riham.gun_fire(fara)
    riham.mele_attack(sadid)

    nafiz_ninja = nafiz.ninja_move(riham)
    fara_ninja = fara.ninja_move(riham)

    nafiz_mele = nafiz.mele_attack(riham)
    fara_mele = fara.mele_attack(riham)

    sadid.ninja_move(riham)
    sadid.gun_fire(riham)

    track_dict.update({fight_cycle:[sadid.name]})

    if(nafiz_ninja == True):
        track_dict[fight_cycle].append(nafiz.name)

    if (fara_ninja == True):
        track_dict[fight_cycle].append(fara.name)



    shihab.release(riham)

    if(shihab.release_condition == False):
        track_dict[fight_cycle].append(riham.name)

print(track_dict)




