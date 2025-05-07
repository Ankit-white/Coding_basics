def loops():
    n = 1234
    count = 0
    while n != 0:
        n = n // 10  # Integer division
        count += 1
    return count

print(loops())
