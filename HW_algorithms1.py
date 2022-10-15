
#1. Compute the sum of digits in all numbers from 1 to n

def sum_numbers(n):

    result = 0

    for i in range(1, n+1):
        result += i
    return result


n = 5
sum = sum_numbers(n)
print(sum)


#2. Find max number from 3 values

a = 124
b = 21
c = 32

def max_number(a,b,c):
    if a > b and a > c: return a
    elif b > a and b > c: return b
    else: return c

max = max_number(a,b,c)
print(max)

#3. Count odd and even numbers

even = 0
odd = 0


def count_odd_even_numbers(even, odd):

    d = 34560

    while d > 0:
        if d % 2 == 0:
            even += 1
        else:
            odd += 1
        d = d // 10
    return even, odd


count = count_odd_even_numbers(even, odd)
print(count)


