import itertools as it

appetizers = ['Mozzarella Sticks', 'Nachos', 'Buffalo Wings', 'Salad', 'Vegetables']
main_dish = ['Chicken', 'Steak', 'Burger', 'Quesadilla', 'Tacos']
desserts = ['Ice Cream', 'Apple Pie', 'Cookie', 'Shake']

print(list(it.product(appetizers, main_dish, desserts)))