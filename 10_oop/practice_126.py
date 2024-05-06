class Person:

    # attributes: name(str), age(int), friends(list of Person objects)
    # when creating Person objects, friends list must be empty
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []

    # methods: add_friend(Person object), remove_friend(Person object)
    # add_friend: prevent duplicates, print Name_of_person already exists

    def add_friend(self,friend):
        if friend in self.friends:
            print(f"{friend.name} already exists")
        else:
            self.friends.append(friend)

    # remove_friend: prevent removing friends that don't exist in the list
        # print Name_of_person is not your friend

    def remove_friend(self,friend):
        if friend not in self.friends:
            print(f"{friend.name} is not your friend")
        else:
            self.friends.remove(friend)

    # Person_Object.show_friends()
        # Ex. Ahmed has two friends Ali and Hassan
            # Ahmed's Friends:
                # Ali
                # Hassan
        # or Ahmed has no friends.. 

    def show_friends(self):
        if self.friends:
            print(f"{self.name}'s friends :")
            for friend in self.friends:
                print(f"    {friend.name}")
        else:
            print(f"{self.name} has no friends")
            

mohamed = Person("mohamed",37)
ali = Person("ali",36)
sara = Person("sara",32)

mohamed.add_friend(ali)
mohamed.add_friend(sara)
mohamed.show_friends()
ali.show_friends()
# mohamed.remove_friend(ali)
# print(mohamed.friends)
# mohamed.remove_friend(ali)