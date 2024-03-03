def sum_of_array_elements():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    array_sum = sum(array)
    print("\nSum of array elements:", array_sum)
sum_of_array_elements()
