number = 17
is_prime = True

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number} bir asal sayidir.")
else:
    print(f"{number} bir asal sayi değildir.")
    