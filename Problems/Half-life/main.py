initial_quantity = int(input())
final_quantity = int(input())
half_life = 0

while final_quantity <= initial_quantity:
    initial_quantity = initial_quantity / 2
    half_life += 1

print(half_life * 12)