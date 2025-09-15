#
# for i in range(2,11,2):
#     print(i)
#
# for i in range(1,11,2):
#     print(i)

# Python program to print prime numbers from 1 to 100

# Define the range

# Python program to print prime numbers from 1 to 100

# Python program to print prime numbers from 1 to 100

# Define the range
start = 1
end = 100

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        # Check if num is divisible by any number from 2 to num-1
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
