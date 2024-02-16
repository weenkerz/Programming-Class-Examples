import itertools


def pent_num(target) -> int:
    return 1 + list(itertools.accumulate([(i * 5) for i in range(target)]))[target - 1]


# target = int(input("For which number would you like to find its pentagonal counterpart: "))
# initial = 1
# for i in range(0, target):
#     addition = i * 5
#     initial += addition

print(pent_num(int(input("For which number would you like to find its pentagonal counterpart: "))))
