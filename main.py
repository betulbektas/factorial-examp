def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    num = int(input("Bir pozitif tam sayı girin: "))

    if num < 0:
        print("Negatif sayılar için faktöriyel hesaplanamaz.")
    else:
        print(f"{num}! = {factorial(num)}")

    if is_prime(num):
        print(f"{num} bir asal sayıdır.")
    else:
        print(f"{num} bir asal sayı değildir.")

if __name__ == "__main__":
    main()
