def count_down(count):
  if count == 0:
    print("Vamos Argentina!\n")
  else:
    print(count)
    return count_down(count - 1)

n = int(input("Enter a number: "))
count_down(n)