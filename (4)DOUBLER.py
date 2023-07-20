#this file will be my game-like learning practice in python


def doubler(stringz):
    word = list(stringz)
    result = []
    for x in word:
        result.append(x*2)
    listToStr = ''.join(result)
    return print(listToStr)

input = "Jamsekun0417" #this is what you change
doubler(input)
