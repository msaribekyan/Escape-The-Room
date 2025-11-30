#Write a function that finds the intersection of two lists without using sets.
def intersection_of_lists (lst1, lst2):
    result = []
    used = [False] * len(lst2)

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if not used[j] and lst1[i] == lst2[j]:
                result.append(lst1[i])
                used[j] = True
                break
    return result

lst1 = [1, 1, 2, 3]
lst2 = [1, 1, 2, 4]
print (intersection_of_lists(lst1, lst2)) #[1, 1, 2]
