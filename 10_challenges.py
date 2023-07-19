#this file will be my game-like learning practice in python

nums = [1,3,4,6,2,3,10,16,203,-2,3,0]

def sorting_algo(list, style):
    groupOfnum = list
    if style == "asc":
        groupOfnum.sort()
        print(groupOfnum)
    elif style == "desc":
        groupOfnum.sort(reverse=True)
        print(groupOfnum)
    elif style == "none":
        print(groupOfnum)
    else:
        print("wrong input")
    pass

sorting_algo(nums, "desc")