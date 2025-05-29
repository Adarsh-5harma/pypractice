# Implementing Stack
my_stack = [2,3,4,5,8,9,6,7]

my_stack.append(10)
my_stack.append(11)
my_stack.append(22)
print(f"the stack is {my_stack}")

# peek means to return top or last element
# [-1] is the position of topmost element
topelemt = my_stack[-1]
print(f"the top element is {topelemt}")

my_stack.pop()
# this will pop the topmost element
print(f"the stack after pop is {my_stack}")

# by checking lengthof stack as 0
# if 0 return true else false
is_empty = len(my_stack) == 0
print(f"is the stack empty {is_empty}")

len_stack = len(my_stack)
print(f"the length of stack is {len_stack}")

