# input - list of integers
# output - sum of all elements <int>


def summ(array):
    if array == []:
        return 0
    return array[0] + summ(array[1:])


mylist = []
print(summ(mylist))
