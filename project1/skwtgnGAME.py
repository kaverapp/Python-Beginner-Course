import random

# start
# 2 display rules
# 3 ask for user for number of time
# ask for the choice of n time
# 4 display result

n = int(input("enter num of plays:"))

desin = {"play": n, "bot": 0, "user": 0}

store = []

snake=1
water=2
gun=3


def play(n):
    if n==0:
        return 1
    user = int(input("entr ur choice"))
    ran = random.randint(1, 3)
    desin["play"] -= 1
    # print(ran,"each recur")
    if user == ran:
        print("tie")
    else:
        if(user==snake and ran==water) or (user==water and ran==gun) or (user==gun and ran==snake):
            desin["user"]+=1
        else:
            desin["bot"] += 1

    play(n - 1)


play(n)

if desin["user"] > desin["bot"]:
    print("user won")
elif desin["user"] < desin["bot"]:
    print("try next time")
else:
    print("tie")
print(desin)