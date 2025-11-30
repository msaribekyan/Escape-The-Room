# Write a function sum_digits(n: int) -> 
# int that returns the sum of the digits in an integer.
def sum_digits (num):
    sum = 0
    if num < 0:
        num = abs(num)
    while num > 0:
        sum+=num % 10
        num //= 10
    return sum
print(sum_digits(1234)) #10

