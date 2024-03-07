x = int(input('Enter the Number:'))

divisors = [i for i in range(1, x) if x % i == 0]

sum_divisors = sum(divisors)

is_perfect = sum_divisors == x

print(is_perfect)



