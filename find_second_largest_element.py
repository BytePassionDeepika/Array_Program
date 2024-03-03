def find_second_largest_element():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    unique_elements = list(set(array)) 
    if len(unique_elements) < 2:
        print("\nThere is no second-largest element in the array.")
    else:
        unique_elements.sort(reverse=True)
        second_largest_element = unique_elements[1]
        print("\nSecond-largest element in the array:", second_largest_element)
find_second_largest_element()
