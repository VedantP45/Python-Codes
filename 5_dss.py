import random
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_random_prime(min_value, max_value):
    if min_value < 2:
        min_value = 2
    while True:
        num = random.randint(min_value, max_value)
        if is_prime(num):
            return num

def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b
    return a


p = generate_random_prime(2, 50)
q = generate_random_prime(2, 50)
print(f"First prime number is {p}")
print(f"First prime number is {q}")

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 1


d = 2
while True:
    if (e * d) % phi == 1:
        break
    else:
        d += 1

msg = int(input("Enter plaintext in numerical form: "))
flag = False

if msg >= n:
    flag = True

while flag:
    print(f"Enter plaintext in numerical form and less than {n}")
    msg = int(input(""))
    if msg < n:
        break

print(f"Original message: {msg}")


print(f"Private key is: ({d}, {n}) which is used for signature generation")
print(f"Public key is: ({e}, {n}) which is used for signature verification")



s = (msg ** d) % n
print(f"Generated signature is: {s}")


verification_result = (s ** e) % n
print(f"Verification result is: {verification_result}")
print(f"Original message is: {msg}")


if verification_result == msg:
    print("Signature verified\n")
else:
    print("Signature verification unsuccessful\n")
