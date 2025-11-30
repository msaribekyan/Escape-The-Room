# Write a function that takes two lists and returns a dictionary mapping elements from the first list to the second (like zip but manually).

def make_dict(lst1, lst2):
    if len(lst1) != len(lst2):
        return 

    dict = {}
    for i in range(len(lst1)):
        key = lst1[i]
        value = lst2[i]
        dict[key] = value

    return dict

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(make_dict(lst1, lst2)) # {1: 'a', 2: 'b', 3: 'c'}
