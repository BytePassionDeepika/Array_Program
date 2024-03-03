def find_unique_elements():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    unique_elements_set = set(array)
    unique_elements_list = list(unique_elements_set)
    print("\nUnique elements in the array:")
    for element in unique_elements_list:
        print(element, end=' ')
find_unique_elements()
