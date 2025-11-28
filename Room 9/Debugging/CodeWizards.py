#Fix the function to properly reverse a dictionary and handle cases where multiple keys may share a value.

def reverse_dict(d):
    return {k: v for v, k in d.items()}

print(reverse_dict({'a': 1, 'b': 2}))
