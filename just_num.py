#this file will be my game-like learning practice in python
Mylist = ["hello", 42, 3, "world"]
def JustNum(lst):
    result = []
    for var in Mylist:
        if type(var) == int:
            result.append(var)
    return result

print(JustNum(Mylist))
