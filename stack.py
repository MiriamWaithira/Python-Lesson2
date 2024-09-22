# These are user-defined data structures
stack = []
print(stack)

stack.append(3)
stack.append(4)
stack.append(11)
stack.append(15)
stack.append(8)

print('The appended stack is:', stack)
print(stack.pop()) #To print the last item in the list

new_stack = [3, 4, 11, 15, 8]
new_stack.remove(3) #To remove 3 from the stack
print('The newer stack is:', new_stack) #Stack without 3