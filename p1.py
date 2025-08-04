def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 2False
    return True

for i in range(1, 50):
    print(f"{i} is prime: {is_prime(i)}")
#prime number
#another
