#  test cases:
# input: [] | output: 0
# input: [1] | output: 1
# input: [1, 6, 343] | output: 3

def element_count(array):
    '''
    Returns the amount of elements in the provided list
        
        Parameters:
            array(list): A list of elements of any data type
            
        Returns:
            element_count(int): the amount of elements in the list
    '''
    if array == []:
        return 0
    return 1 + element_count(array[1:])

mylist = [1, 6, 343]
print(element_count(mylist), element_count.__doc__)