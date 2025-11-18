# Write a function that merges two sorted lists into a single sorted list without duplicates.
#Write a function that merges two sorted 
# lists into a single sorted list without duplicates.

def merge_two_lists(lst1, lst2):
    lst1.sort()
    lst2.sort()

    set1 = set(lst1)
    set2 = set(lst2)

    new_set = set1 | set2
    new_list = list(new_set)
    new_list.sort()

    return new_list

lst1 = [-4, 9, 3, 5, 6]
lst2 = [7, 3.5, 4, -2, 0]
print(merge_two_lists(lst1, lst2)) #[-4, -2, 0, 3, 3.5, 4, 5, 6, 7, 9]
