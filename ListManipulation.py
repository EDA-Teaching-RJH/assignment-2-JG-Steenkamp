numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers.extend([7, 8])
numbers.sort()
numbers = [num for num in numbers if num != 1]
print(numbers)
