def calc_area_rectangle(x, y):
    return x * y


rec1 = [5, 6]
rec2 = (10, 100)

# print(calc_area_rectangle(rec1[0], rec1[1]))
# print(calc_area_rectangle(rec2[0], rec2[1]))

print(calc_area_rectangle(*rec1))
print(calc_area_rectangle(*rec2))
