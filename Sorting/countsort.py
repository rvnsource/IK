from collections import OrderedDict

my_ordered_dict = OrderedDict()




for i in arr:
    my_ordered_dict[arr[i]] += 1


# Get the first key-value pair
first_key = next(iter(my_ordered_dict))
first_value = my_ordered_dict[first_key]

print("First key:", first_key)
print("First value:", first_value)
