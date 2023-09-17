from random import  randint
# task 1
numbers = []
sum_odd_numbers = 0
sum_even_numbers = 0
product_numbers = 1
start_numbers = 0
end_numbers = 0
start_info = True
sum_numbers = 0
product_numbers1 = 1
sum_neg_numbers = 0
for i in range(10):
    numbers.append(randint(-10, 10))
    print(numbers[i], end=" ")
    if numbers[i] < 0:
        sum_neg_numbers += numbers[i]
    if numbers[i] % 2 == 0:
        sum_even_numbers += numbers[i]
    else:
        sum_odd_numbers += numbers[i]
    if i % 3 == 0:
        product_numbers *= numbers[i]
    if numbers[i] > 0 and start_info:
        start_info = False
        start_numbers = i
    elif numbers[i] > 0:
        end_numbers = i

while start_numbers < end_numbers :
    sum_numbers += numbers[start_numbers]
    start_numbers += 1
start_numbers = numbers.index(min(numbers))
end_numbers = numbers.index(max(numbers))
if start_numbers < end_numbers:
    while start_numbers < end_numbers :
        product_numbers1 *= numbers[start_numbers]
        start_numbers += 1
else:
    while start_numbers > end_numbers:
        product_numbers1 *= numbers[end_numbers]
        end_numbers += 1
print()
print("sum of negative numbers {}, sum of even numbers {}, sum of odd numbers {}, product of multiples of 3 {}, product\
between minimum and maximum {}, sum between positiv {}".format(sum_neg_numbers,sum_even_numbers,sum_odd_numbers,\
product_numbers, product_numbers1, sum_numbers))

