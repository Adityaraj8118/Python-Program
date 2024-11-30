import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '.-@!#$%^&*'
number = '123456778'

all = lower + upper + number + symbol
length = 10 
password = "".join(random.sample(all, length))
print ("The Generated Password is :", password)
