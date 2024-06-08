import random
list = ['sharddha','namita','saud','tanaya','pruthika','sanket','netra','robert','aashish','abhishek','anuj','krushna','virendra']
print(random.choices(list))
#k is length for list
print(random.choices(list,k=4))

random.shuffle(list)

print(random.randint(1,10))
#otp generate, "".join is used for join strings
print("".join(random.sample('1234567890',k=4)))
