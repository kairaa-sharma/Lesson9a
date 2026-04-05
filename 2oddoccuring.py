def printtwoodd(array, size):
    xorof2 = array[0]
    x = 0
    y = 0
    setbit = 0

    for i in range(1, size):
        xorof2 = xorof2 ^ array[i]
    setbit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if(array[i] & setbit):
            x = x ^ array[i]
        else:
            y = y ^ array[i]

    print("The 2 odd elements are", x,"and ",y)

array = []
array_size = int(input("Enter the size of the array: "))
for i in range(0, array_size):
    z = int(input("Enter element. "))
    array.append(z)

printtwoodd(array, array_size)



