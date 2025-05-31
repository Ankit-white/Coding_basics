def loops(): #defining a function
    n = 1234
    count = 0
    while n != 0: # while loop check for the condition if true code runs inside the loop if it falls code will jump out of loop
        n = n // 10  # Integer division
        count += 1 # count = count +1
    return count # returning count value to the functon

print(loops()) # calling the function
