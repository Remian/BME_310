from User_Class import user
from Abstract_Class_Methods import  Abstract_Methods

class Villain(user,Abstract_Methods):


    costume = "bullet proof jacket"
    life = 300

    def mele_attack(self, target_user):
        target_user.life = target_user.life - 5
        print(self.name + " says : Take that mele attack you scar face "+ target_user.name)

    def ninja_move(self, target_user):
        target_user.life = target_user.life - 10
        print(self.name + " says : Take that ninja attack you scar face " + target_user.name)

    def gun_fire(self, target_user):
        target_user.life = target_user.life - 40
        print("\n"+self.name + " says : Firing my big gun!! Boom Boom!! You Scar Faced " + target_user.name + "\n")