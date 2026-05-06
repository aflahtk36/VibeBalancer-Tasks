numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
#largest number
largest=max(numbers)
#smallest number
smallest=min(numbers)
#sum of numbers
total=sum(numbers)
#sum of squares
sum_of_squares=0
for num in numbers:
    sum_of_squares = sum_of_squares + (num * num)

#finding prime numbers
primes=[]
for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

# Display results
print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Sum of squares:", sum_of_squares)
print("Primes:", primes)