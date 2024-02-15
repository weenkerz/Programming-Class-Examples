import itertools as it

# My magnum opus
print(list(set([i for i in [int(''.join(n)) for o in (list(it.permutations(lst, m) for m in range(1, len(lst)))) for n in o] if all(i % j != 0 for j in range(2, round(i ** 0.5) + 1)) and i != 1 and i != 0])) if (lst := [i for i in input('Please enter a number: ')]) else ())
