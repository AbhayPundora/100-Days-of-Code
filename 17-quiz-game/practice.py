class User:
    def __init__(self, user_id, user_age):
        self.id = user_id
        self.age = user_age
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1




user1 = User(1, 20)
user2 = User(2, 32)
# user1.id = "001"
# user1.age = 8

# print(user1.id)
# print(user2.age)
# print(user1.followers)
# print(user2.followers)

user1.follow(user2)
print(user1.following)
print(user1.followers)
print(user2.followers)
print(user2.following)
