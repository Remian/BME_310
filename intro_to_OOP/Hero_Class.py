from User_Class import user
from Abstract_Class_Methods import  Abstract_Methods

class Hero(user, Abstract_Methods):
    costume = "wears underpants over trousers"
    life = 500





    def mele_attack(self, target_user):
        target_user.life = target_user.life - 10
        print(self.name + " says : Take that mele attack you scar face " + target_user.name)

    def ninja_move(self, target_user):
        target_user.life = target_user.life - 25
        print(self.name + " says : Take that ninja attack you scar face " + target_user.name)

    def gun_fire(self, target_user):
        target_user.life = target_user.life - 5
        print(self.name + " says : though my gun is small! BOOM BOOM!! Take that " + target_user.name)