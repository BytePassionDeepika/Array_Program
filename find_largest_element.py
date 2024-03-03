def find_largest_element():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    max_element = max(array)
    print("\nLargest element in the array:", max_element)
find_largest_element()
