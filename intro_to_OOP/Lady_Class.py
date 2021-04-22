from User_Class import user
from Abstract_Class_Methods import Abstract_Methods


class Lady(user, Abstract_Methods):
    costume = "biyer shari"
    release_condition = False


    def release(self, villain_user):
        if villain_user.life < 5:
            self.release_condition = True
            print(villain_user.name + " is dead. Love is secured. Peace on earth!")
