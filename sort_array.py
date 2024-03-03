def sort_array():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    ascending_order_array = sorted(array)
    descending_order_array = sorted(array, reverse=True)
    print("\nArray in ascending order:", ascending_order_array)
    print("Array in descending order:", descending_order_array)
sort_array()
