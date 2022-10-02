lst=[1,2,3,4,5,6,7]
print("original list: ",lst)
result=map(lambda x: x + x + x,lst)
print("Triple of list Numbers: ")
print(list(result))