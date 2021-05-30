#1. Write a python code to remove an element from a tuple.
def remove_from_tuple():
    mytuple = ("apple", "banana", "cherry")
    y = list(mytuple)
    y.remove("apple")
    mytuple = tuple(y)
    print(mytuple)


#2. Replace the last element in the list with the string 'last' using list comprehension and tuples
def replace_last_element():
    mytuple = ("apple", "banana", "cherry")
    y = list(mytuple)
    y = y[:-1] + ['last']
    mytuple = tuple(y)
    print(mytuple)


#3. Extract only the strings from the following list using list comprehension : slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
def extract_only_strings():
    slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
    for element in slist:
        if (type(element) == str):
            print(element)


#4. Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest.
def generate_matrix():
    elements = ['X', '_', '_', '_', 'X', '_', '_', '_', 'X']

    print( ''.join(' '*(n%3!=0)+l+'\n'*(n%3==2) for n,l in enumerate(elements)))


if __name__ == '__main__':
    remove_from_tuple()
    replace_last_element()
    extract_only_strings()
    generate_matrix()
