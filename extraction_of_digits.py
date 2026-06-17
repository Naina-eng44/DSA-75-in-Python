#  1. reverse a number

n = 5873
num = n
while num > 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10
    
    
#  2. count digits

n = 5673
num = n
count = 0
if num == 0:
    count = 0
else:
    while num > 0:
        count += 1
        num = num //10
print(count)    


from math import *
def count_digits(num):
    return int(log10(num)+1)


#  3. check palindrome

n=1234
num = n
result = 0
while num>0:
    last_digit = num % 10
    result = (result*10) + last_digit
    num = num//10
print(n == result)


#  4. check armstrong number

n=153
num=n
nod=len(str(n))
total = 0
while num > 0:
    last_digit = num % 10
    total = total + (last_digit ** nod)
    num = num//10
print(total == n)


#  5. print factors/ divisors of a given number

n = 20

result =[]
for i in range(1,n+1):
    if n % i == 0:
        result.append(i)
print(result)
        


