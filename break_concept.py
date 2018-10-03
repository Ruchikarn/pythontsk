for i in range(100):
    print('Hello World', i)

    if i == 50:
        break


def prime_or_composite(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime


print(prime_or_composite(7))
print(prime_or_composite(10))

for i in range(2, 11):
    if i % 2 == 0:
        print(i ** 2)
    else:
        print(i ** 3)

