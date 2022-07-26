# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# () - tuple
# A tuple is a sequence of items that can't be changed (immutable).

# [] - list
# A list is a sequence of items that can be changed (mutable).

# {} - dictionary or set

# class Customers:
#     greeting = "Welcome to the Coffee Palace"
#
#
# customer_1 = Customers()
# customer_1.name = "Samirah"
# customer_1.beverage = "Iced caffe latte"
# customer_1.food = "Cinnamon roll"
# customer_1.total = 255
#
# customer_2 = Customers()
# customer_2.name = "Jerry"
# customer_2.beverage = "Caramel macchiato"
# customer_2.food = "Glazed doughnut"
# customer_2.total = 230
#
# print(Customers.greeting)
# print(customer_1.beverage)
# print(customer_2.food)

# print(217 * 6)
# print(600 + 35234)
# print(67 // 12)
# print(56329 % 982)
# print(34 ** 5)

# my_age = 22
# mom_age = 61
# sister_age = 29

# print(mom_age < sister_age and my_age == 22)
# print(mom_age == 61)
# print(mom_age > 34 or sister_age == 22)
# print(mom_age >= 54)
# print(not(sister_age <= 400 and my_age == 22))

# Loops
# colors = ["red", "blue", "green", "cyan", "magenta", "yellow", "black"]
# things = ["car", "bike", "notebook", "pen"]
#
# for i in colors:
#     for t in things:
#         print(i, t)
#
# x = range(8)
#
# for y in x:
#     print(y)

# i = 1
#
# while i <= 10:
#     print(i)

# furniture = ["table", "chair", "cabinet", "desk", "couch"]
#
# for f in furniture:
#     if f == "cabinet":
#         continue
#     print(f)
#
# i = 1
#
# while i < 15:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 15")

# Inheritance
# class Guest:
#     def __init__(self, first, last, interest, phone):
#         self.first = first
#         self.last = last
#         self.interest = interest
#         self.phone = phone
#
#
# g1 = Guest("abdul", "yakol", "p*rn", 696969)
# g2 = Guest("Lim", "Lupes", "c*king", 696969)
#
# print(g1.first)
# print(g2.interest)


# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     def display(self):
#         print("(parent class/User) Username:", self.username, "password:", self.password)
#
#     def kipay(self):
#         print('olol')
#
#
# class Admin(User):
#     def __init__(self, username, password, code):
#         self.code = code
#         User.__init__(self, username, password)
#         # super().__init__(username, password)
#
#     def display69(self):
#         super().display()
#         super().kipay()
#         print("(subclass/Admin) Username:", self.username, "password:", self.password, "code:", self.code)
#
#
# u1 = User("kipay", "kipay123")
# a1 = Admin("zep", "bilat123", "code 86")
#
# u1.display()
# a1.display69()


# class ClubMembers:
#     def __init__(self, name, birthday, age, favorite_food, goal):
#         self.goal = goal
#         self.favorite_food = favorite_food
#         self.age = age
#         self.birthday = birthday
#         self.name = name
#
#     def display_member(self):
#         print("Name:", self.name)
#         print("Birthday:", self.birthday)
#         print("Age:", self.age)
#         print("Favorite Food", self.favorite_food)
#         print("Goal:", self.goal)
#
#
# class ClubOfficer(ClubMembers):
#     def __init__(self, name, birthday, age, favorite_food, goal, position):
#         self.position = position
#         ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)
#
#     def display_officer(self):
#         print("Name:", self.name)
#         print("Position:", self.position)
#         print("Birthday:", self.birthday)
#         print("Age:", self.age)
#         print("Favorite Food", self.favorite_food)
#         print("Goal:", self.goal)
#         print("Position:", self.position)
#
#
# cooking_club_m_1 = ClubMembers("Tom", "January 16", 14, "chickin", "To be a Lord")
# cooking_club_m_1.display_member()
#
# cooking_club_o_1 = ClubOfficer("Vera", "June 22", 16, "beef", "To be a ", "Prisidint")
# cooking_club_o_1.display_officer()

# Dictionaries

# shopping_list = {
#     "weird hat": 100,
#     "purple rug": 450,
#     "old books": 200,
#     "stuff elephant": 50
# }
#
# print(shopping_list)
#
# shopping_list['platstic ring'] = 69
# shopping_list['platstic ring'] = 6969
#
# print(shopping_list)
#
# basketball_teams = {
#     "Crouching Tigers": ["Jacob", "Ken", "Kevin", "Roy", "Joe"],
#     "Hidden Dragon": ["acob", "en", "evin", "oy", "oe"]
# }
#
# print(basketball_teams)
#
# basketball_teams.update({"Team Bilat": ["zep 1", "zep 2", "zep 3", "zep 4", "zep 5"]})
#
# print(basketball_teams)
#
# print(basketball_teams['Team Bilat'])
#
# zep = zip(shopping_list, basketball_teams)
#
# print(list(zep))
#
# dic = dict(zip(shopping_list, basketball_teams))
#
# print(dic)
#
# print(basketball_teams.get('Hidden'))
# print(basketball_teams.pop('Hidden Dragon'))
# print(basketball_teams.values())
# print(basketball_teams.items())


employee_1 = {
    "Name": "Frank",
    "Position": "Sales Rep",
    "Email": "frank@companay.com"
}

for key, value in employee_1.items():
    print(key, value)

for name in employee_1.keys():
    print(name)

foods = {
    "Mcdo": ["chicken", "sundae"],
    "Jolibee": ["chicken", "spagetti"],
    "KFC": ["gravy", "mashed potato"],
    "PizzaHut": ["pizza", "pasta"]
}

for item in foods.values():
    print(item)
    print(item[0])

cat = {
    1: {"name": "Mengmeng", "Age": 5, "color": "white"},
    2: {"name": "Posasa", "Age": 99, "color": "black"},
}

print(cat.items())

for i in cat:
    print(cat[i])
