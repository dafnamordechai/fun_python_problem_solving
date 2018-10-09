#
# Brute force / straightforward
#

#hard codded for vlues
def solution_1(num):
    if (num == 4):
        return 5
    return 4

#dynamic values changes (run time)
def solution_2(num):
    my_dictionary = {4: 5, 5: 4}
    return my_dictionary.get(num, 'default')

#
# Math tricks
#
def solution_3(num):
    if num != 0:
        return (20/num)
    return 0

def solution_4(num):
    return (9-num)

def solution_5(num):
    return (1^num)

def solution_6(num):
    a = [0,1,2,3,5,4]
    return a.index(num)

def main():
    for i in range(4,6):
        print("NEW LOOP" , i)
        print(solution_1(i))
        print(solution_2(i))
        print(solution_3(i))
        print(solution_4(i))
        print(solution_5(i))
        print(solution_6(i))

main()