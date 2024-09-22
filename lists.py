students_age = [24, 23, 22]
print(students_age)
print(students_age[-2]) #Will print 23 because it starts from right to left and there is no -0

my_list = ['Student', 'Python', 'School', 'Age']
#will print out index 0 and 1
print(my_list[0:2]) #will exclude index 2
print(my_list[2:]) #will print starting from index 2 to the end
print(my_list[:3]) #will print from the beginning to index 2
print(my_list[-1:-4])
print(my_list[-4:-1])

#Appending to add an item into the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers.append(9)
print('After append:', numbers)

#Extending- uses the extend() method to add all items of one list to another
prime_numbers = [2, 3, 5]
print('List1:', prime_numbers)

even_numbers = [4, 6, 8]
print('List2:', even_numbers)

prime_numbers.extend(even_numbers)
print('List after appending:', prime_numbers)