#Print out all odd numbers between 0 and 100.
start = 0
end = 100
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")
        