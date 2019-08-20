grades = [73, 67, 38, 33]

for x in grades:
    multi = ((int(x / 5) + 1) * 5)
    gap = multi - x
    print(multi, x, gap, x if x < 38 else multi if gap < 3  else x)
