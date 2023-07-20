#this file will be my game-like learning practice in python
import secrets #this is like random module, but better
import string

secrets.randbits
resultword = ""
strong_plength = [12, 13, 14, 15, 16]
weak_plength = [ 5, 6, 7, 8]

def PassGen(option):
    global resultword
    if option == 0:
        randword = secrets.choice(string.ascii_lowercase)
        resultword += randword
    elif option == 1:
        randword = secrets.choice(string.ascii_uppercase)
        resultword += randword
    elif option == 2:
        randword = secrets.choice(string.digits)
        resultword += randword
    elif option == 3:
        randword = secrets.choice(string.punctuation)
        resultword += randword                      
    pass

def strongPassGen():
    for i in range(secrets.choice(strong_plength)):
        PassGen(secrets.randbelow(4)) #u can change the parameter to 1,2,3,4 

def weakPassGen():
    for i in range(secrets.choice(weak_plength)):
        PassGen(secrets.randbelow(3)) #u can change the parameter to 1,2,3,4
def default():
    print("incorrent input")


kindOfPass = { "1": strongPassGen, '2': weakPassGen}
input = input("Pass gen: \n type 1 if strong \n type 2 if weak \n")
kindOfPass.get(input, default)()

print(resultword)
