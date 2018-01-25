import time

#Setting up register
#defining people's characteristics
class Person:
    def __init__(self, height, color, name):
        self.h = height
        self.c = color
        self.n = name

#Defining characteristincs
def set_variable(question, order):
    x = input("What is person " + str(order) + "'s " + str(question) + "?\n")
    return x

#Person list, choose which person in list, print names
def add_people(number):
    p =[]
    for t in range(number):
        p.append(str("person" + str(t+1)))
        p[t] = Person(set_variable("height", (int(t)+1)), set_variable("hair color", (int(t)+1)), set_variable("name", (int(t)+1)))
    time.sleep(0.5)
    print("People registered:")
    for item in p:
        time.sleep(0.5)
        print(str("- " + str(item.n)))
    return p

#Choosing characteristincs
#Choose Person
def choose_person(choose_name, list_name):
    for item in list_name:
        if choose_name == item.n:
            time.sleep(0.5)
            print(str(choose_name + ":"))
            time.sleep(0.5)
            print(str("Height: " + str(item.h)))
            time.sleep(0.5)
            print(str("Hair color: " + str(item.c)))


start = True
while start == True:
    people_list = add_people(int(input("How many people do you want to register? \n")))
    time.sleep(0.5)
    choose_person((input("What person's information do you want?")), people_list)
