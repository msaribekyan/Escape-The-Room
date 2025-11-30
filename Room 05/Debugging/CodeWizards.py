#Fix the code to return a list of squares of all numbers (integers only) in a list.

def squares(lst):
    result = []
    for num in lst:
        if type(num) == int:
            result.append(num**2)
    return result

print(squares([1, 2, "three", 4, "five"]))

