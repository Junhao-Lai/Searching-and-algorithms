def bin_search(number,key):
  low = 0
  high = len(number) - 1

  while high >= low:
    mid = (high + low)//2
    if number[mid] > key:
      high = mid - 1
    elif number[mid] < key:
      low = mid + 1
    else:
      return mid
  return - 1

number = [2,5,6,14,16,24,32,63]
print("NUMBERS: ", end = ' ')
for num in number:
  print(str(num),end = ' ')
print()

key = int(input("Enter your target value："))
key_index = bin_search(number,key)


if key == -1:
  print(str(key),'was not found')
else:
  print(str(key),"is found at index", str(key_index))

