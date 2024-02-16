# target = int(input("Please enter a number: "))
# triangles = [i for i in range(target + 1)]
# num = 0
# count = 0

# while count < target:
#     for i in triangles:
#         num += i
#         count += 1

# print(num)

########################################################################################################################

import itertools


def tri_num(target) -> int:
    return list(itertools.accumulate([i for i in range(target + 1)]))[target]


print(tri_num(int(input("Please enter the number: "))))

########################################################################################################################
