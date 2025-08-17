"""Prime number checker script.

This script defines a function to check if a number is prime
and prints prime status for numbers from 1 to 49.
"""

def is_prime(number):
    """Check if a given number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def main():
    """Run the prime number check for numbers 1 to 49."""
    for num in range(1, 50):
        print(f"{num} is prime: {is_prime(num)}")


if __name__ == "__main__":
    main()
