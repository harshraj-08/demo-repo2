names = input("ENter names with comma at the end ! \n")
op = names.split(",")
print(op)

import random
# random_index = random.randint(0,(len(op)-1))
# person_who_will_pay = (op[random_index])
# print(person_who_will_pay+" is going to buy the meal !")

person_who_will_pay = random.choice(op)
print(person_who_will_pay+" is going to buy a meal today !")







