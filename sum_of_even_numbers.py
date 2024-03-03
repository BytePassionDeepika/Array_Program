def sum_of_even_numbers():
    n = int(input("Enter the size of the array: "))
    array = []
    print("Enter the array elements:")
    for i in range(n):
        element = int(input())
        array.append(element)
    even_numbers_sum = sum(num for num in array if num % 2 == 0)
    print("\nSum of even numbers in the array:", even_numbers_sum)
sum_of_even_numbers()
