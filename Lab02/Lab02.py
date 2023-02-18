# to print odd Numbers 0 to 100
 
start, end = 0, 100
 
# iterating each number in list
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")
