#this file will be my game-like learning practice in python

def binConverter(num):
    bin_list = []
    while True:
        remainder = num%2
        num = num//2
        bin_list[:0] = [remainder]
        if num == 1:
            remainder = num%2
            num = num//2
            bin_list[:0] = [remainder]
            break
    bin_lst_str = ''.join(map(str, bin_list))
    return print(bin_lst_str)

binConverter(156)

#the actual solution
def decimal_to_binary(num):
    if num == 0:
        return ''
    return decimal_to_binary(num // 2) + str(num % 2)
number = 10
binary = decimal_to_binary(number)
print(binary)