def print_elements_at_even_positions():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    print("\nElements at even positions:")
    for i in range(0, n, 2):
        print(array[i], end=' ')
print_elements_at_even_positions()
