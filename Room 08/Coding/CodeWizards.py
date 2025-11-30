# Write a function that receives a list of dictionaries and returns a new dictionary that merges them all together.
def dictionary(lst):
    if not isinstance(lst,list):
       raise TypeError("The input should be a list consisting of dictionaries")
    for dict_ in lst:
        if not isinstance(dict_,dict):
            raise ValueError("The input should be a list consisting of dictionaries")
    if len(lst)==0:
        return {}
    merge_dict=lst[0].copy()
    for dict_ in lst[1:]:
        for key,value in dict_.items():
            if key in merge_dict.keys():
                if merge_dict[key]==value:
                    continue
                if not isinstance(merge_dict[key],list):
                    merge_dict[key]=[merge_dict[key]] 
                merge_dict[key].append(value)
            else:
                merge_dict[key]=value
    return merge_dict
try:
    print(dictionary([{1:'a'},{2:'b'}]))#output is {1: 'a', 2: 'b'}
except (ValueError,TypeError) as e:
    print("ERROR:",e)
