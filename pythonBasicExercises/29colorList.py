color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color_list_3 = []

for element in color_list_1:
    if element not in color_list_2:
        color_list_3.append(element)

print(set(color_list_3))