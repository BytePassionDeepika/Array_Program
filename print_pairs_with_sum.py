def print_pairs_with_sum():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    required_sum = int(input("Enter the required sum: "))
    print(f"\nPairs with the sum {required_sum}:")
    for i in range(n):
        for j in range(i+1, n):
            if array[i] + array[j] == required_sum:
                print(f"({array[i]}, {array[j]})", end=' ')
print_pairs_with_sum()
