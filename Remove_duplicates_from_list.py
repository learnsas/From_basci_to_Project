ls = []
num = int(input("Please enter how many numbers of list you want: "))

for i in range(num):
    ls.append(int(input(f'Please enter the number {i+1}: ')))

print(ls)

unique = []
for i in ls:
    if i not in unique:
        unique.append(i)


print(unique)