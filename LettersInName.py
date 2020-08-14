
def letters(name):
    name = name.lower()
    name_set = set(name)
    result = ""
    for letter in name_set:
        result += letter + " "

    return result.upper()

name = input("Enter your name: ")
print("The letters that are in your name are",letters(name))