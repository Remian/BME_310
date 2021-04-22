from User_Class import user
from Abstract_Class_Methods import  Abstract_Methods


class Buddy(user, Abstract_Methods):
    costume = "Whatever Robin wears"
    life = 100


    def mele_attack(self, target_user):
        if (self.check_if_alive() == True):
            pass
        else:
            target_user.life = target_user.life - 5
            print(self.name + " says : Take that mele attack you scar face " + target_user.name)
            return True

    def ninja_move(self, target_user):
        if (self.check_if_alive() == True):
            pass
        else:
            target_user.life = target_user.life - 10
            print(self.name + " says : Take that ninja attack you scar face " + target_user.name)
            return True

    def gun_fire(self, target_user):
        if (self.check_if_alive() == True):
            pass
        else:
            target_user.life = target_user.life - 5
            print(self.name + " says : though my gun is small! BOOM BOOM!! Take that " + target_user.name)
            return True

    def check_if_alive(self):
        if (self.life < 1):
            print("\n" + self.name + " says: Listening Pink Floyed in heaven.\n")
            return True
        else:
            False

