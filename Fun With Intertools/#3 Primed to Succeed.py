import itertools


def prime_permutations(lst_1) -> list:    # Take all permutations using every digit in said number as tuples
    combos = []
    for i in range(1, len(lst_1)):
        combos += itertools.permutations(lst_1, i)
    combos = [''.join(i) for i in combos]    # Combine elements inside tuples
    combos_2 = []    # Remove duplicates
    [combos_2.append(int(i)) for i in combos if int(i) not in combos_2 and
     all(int(i) % j != 0 for j in range(2, round(int(i) ** 0.5) + 1)) and int(i) != 1 and int(i) != 0] # Filter primes

    return combos_2


# Accept user imputed number as a list of strings
while True:
    try:
        print(prime_permutations([i for i in input('Please enter a number: ')]))
        break
    except:
        print(f'Please try a number {chr(129299)}')
