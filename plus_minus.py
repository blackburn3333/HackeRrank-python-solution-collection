test_array = [-4, 3, -9, 0, 4, 1  ]
array_length = len(test_array)

positive_numbers = 0
negative_numbers = 0
zero_numbers = 0

for x in test_array:
    if x > 0:
        positive_numbers = positive_numbers + 1
    elif x < 0:
        negative_numbers = negative_numbers + 1
    elif x == 0:
        zero_numbers = zero_numbers + 1

#print(positive_numbers,negative_numbers,zero_numbers)

def add_decimal(number):
    print(format(number,'6f'))

add_decimal(positive_numbers/array_length)
add_decimal(negative_numbers/array_length)
add_decimal(zero_numbers/array_length)
