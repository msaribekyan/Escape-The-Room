# Write a function that takes a list of integers and returns a new list containing only the prime numbers.
import math
def prime_numbers(integer_list):
    prime_list=[]
    for item in integer_list:
        sqrt_item=math.sqrt(item)
        is_prime=True
        if item==1:
            is_prime=False
        else:
            for num in range(2,int(sqrt_item+1)):
                if item%num==0:
                    is_prime=False
                    break
        if is_prime:
            prime_list.append(item)
    print(prime_list)
prime_numbers([1,2,3,4]) #output is [2,3]
