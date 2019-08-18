print ("SUM of Min and Max")

numbers = [1,5,3,4,2]


min_set = (sorted(numbers, reverse=False))
max_set = (sorted(numbers, reverse=True))

min_sum = sum(min_set[:4])
print (min_sum)
#print (sum(minimum[:4]))
