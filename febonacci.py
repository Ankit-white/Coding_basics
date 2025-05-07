def fabonacci (n):
    feb = [0,1]
    x = 0
    for i in range (1,n):
        x = feb[i] + feb[i-1]
        feb.append(x)
    return feb
        
print(fabonacci (10) )