#Fix the function so it correctly multiplies all elements of a list.

def multiply_elements(lst):
    product = 0
    for num in lst:
        product *= num
    return product

print(multiply_elements([1, 2, 3, 4]))