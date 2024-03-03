def read_and_display_array():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    print("\nArray elements:")
    for element in array:
        print(element, end=' ')
read_and_display_array()
