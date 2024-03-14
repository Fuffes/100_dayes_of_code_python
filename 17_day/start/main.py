class User:

    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_one = User(name="Dory", user_id=1)
user_two = User(name="Masha", user_id=2)

user_one.follow(user_two)

print(user_one.following, user_one.followers)

