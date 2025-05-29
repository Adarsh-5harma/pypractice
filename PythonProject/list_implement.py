my_list = [3,5,1,6,5,8]
my_list.append(10)
my_list.sort()

print(f"the sorted output is {my_list}")

# max = max(my_list)
# min = min(my_list)

# print(f"the max value is {max}")
# print(f"the min value is {min}")

min = my_list[0]
max = my_list[0]

for i in my_list:
    if i < min:
        min = i
    if i > max:
        max = i

print(f"the min value is {min}")
print(f"the max value is {max}")