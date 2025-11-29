#Fix the function to properly reverse a dictionary and handle cases where multiple keys may share a value.

def reverse_dict(d):
    return {k: v for v, k in d.items()}

print(reverse_dict({'a': 1, 'b': 2}))

# my version 
def reverse_dict(d):
    rev_dict={}
    for k, v in d.items():
        if v not in rev_dict:
            rev_dict[v]=k
        else:
            if not isinstance(rev_dict[v],list):
                rev_dict[v]=[rev_dict[v]] 
            rev_dict[v].append(k)
    return rev_dict
print(reverse_dict({'a': 1, 'b': 2}))#output is {1: 'a', 2: 'b'}
