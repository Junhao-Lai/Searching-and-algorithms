def search(number,key):
  for i in range(len(number)):
    if number[i] == key:
      return i
  return -1

number = [1,2,3,4,5,6,7,8,9]
print("Numbers: ", end=" ")
for num in number:
  print(str(num), end=" ")
print()

key = int(input("Target Value: "))
key_index = search(number,key)

if key_index == -1:
  print(str(key),"was not found")
else:
  print("Found",str(key),"@ index", str(key_index))

