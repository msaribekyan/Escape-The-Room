# Write a function that takes a list of integers and returns a new list containing only the prime numbers.
import math
def prime_numbers(integer_list):
    prime_list=[]
    for item in integer_list:
        if item < 2:
            continue

        sqrt_item=int(math.sqrt(item))
        is_prime=True

        for num in range(2, sqrt_item + 1):
            if item % num == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(item)
    return prime_list
print(prime_numbers([0, -1, 2, 3])) #output is [2,3]
