def insertion_sort(numbers):
    for i in range(1, len(numbers)): #从index1 到最后
        j = i
        # Insert numbers[i] into sorted part 
        # stopping once numbers[i] in correct position
        while j > 0 and numbers[j] < numbers[j - 1]: #check L > R
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j = j - 1


numbers = [2,6,5,1,3,4]
print('UNSORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()
 
insertion_sort(numbers)
print('SORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()