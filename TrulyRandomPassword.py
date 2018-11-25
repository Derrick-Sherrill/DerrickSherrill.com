import string
from random import *
import datetime

now = datetime.datetime.now()
seed(now)
characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(choice(characters) for x in range(randint(8,16)))
password2 = "".join(choice(characters) for x in range(randint(7,15)))

print(password)
print(password2)
