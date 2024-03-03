def print_element_frequencies():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    frequency_dict = {}
    for element in array:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    print("\nElement frequencies:")
    for element, frequency in frequency_dict.items():
        print(f"Element {element}: {frequency} times")
print_element_frequencies()
