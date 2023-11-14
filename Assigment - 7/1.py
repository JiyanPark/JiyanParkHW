def chop(lst):
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
def middle(new_list):
    if len(new_list) >= 2:
        return new_list[1:-1]

list = [1, 2, 3, 4]
print("my list before call chop function =>", list)
chop(list)
print("my list after call chop  function => ", list)  


list = [1, 2, 3, 4]  
print("\nmy list before call middle function =>", list)
middle_list = middle(list)
print("my list after call middle function =>",list)
print("new list after call middle function => ", middle_list)  