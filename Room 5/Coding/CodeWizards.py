#Write a function that takes a list and returns a list of tuples containing (element, index) only for even-indexed elements.
def for_list(input_list):
    if not isinstance(input_list, list) or not input_list:
        raise ValueError("Input must be a non-empty list")
    result_list=[]
    for index, value in enumerate(input_list):
        if index%2==0:
            result_list.append((value,index))
    return result_list
try:
    print(for_list([1, 2, 3, 4, 5]))
except ValueError as e:
    print("Error:", e)
