number = input(">")
# name = number.split()

dicton = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

string=""
for i in number:
    string += dicton.get(i,"!") + " "

print(string)