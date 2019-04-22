ls = []
num = int(input("Please enter how many numbers of list you want: "))

for i in range(num):
    ls.append(int(input(f'Please enter the number {i+1}: ')))

print(ls)
largest = 0
for i in ls:
    if i > largest:
        largest = i
    else:
        largest = largest

print(f"from given list largest number is {largest}")


