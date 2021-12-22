# Python program to print odd Numbers in a List

# list of numbers
list1 = range(0,101)
  
# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 != 0:
       print(num, end = " ")
