#For Python: Write a function that receives a list of tuples and returns a dictionary grouping by the first item of each tuple.
#Example: [('a', 1), ('b', 2), ('a', 3)] → {'a': [1, 3], 'b': [2]}

def make_dict(lst):
    res_dict = {}
    for el in lst:
        key = el[0]
        values = el[1:]
        if key not in res_dict:
            res_dict[key] = []
        res_dict[key].extend(values)
    return res_dict

print(make_dict([('a', 1, 5), ('b', 2), ('a', 3)])) #{'a': [1, 5, 3], 'b': [2]} 
