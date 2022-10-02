lst = [4,5,2,9]
print("Original list: ",lst)
def square(data):
    return data ** 2

square_lst = list(map(square,lst))
print("Square the elements of the list: ")
print(square_lst)