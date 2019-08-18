test_array = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
test_len = (len(test_array) - 1)

a_diagonal = []
b_diagonal = []
for x in range(len(test_array)):

    a_diagonal.append(test_array[x][x])
    b_diagonal.append(test_array[test_len-x][x])

a_diagonal_sum = sum(a_diagonal)
b_diagonal_sum = sum(b_diagonal)
print(abs(a_diagonal_sum - b_diagonal_sum))

