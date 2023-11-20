from functions import *

test = User('Luca')
test.sport.append(test.Sport("Bouldern", 10, "steinbock"))
print(test.__dict__.values())
# print(test.Sleep.__dict__.keys())
