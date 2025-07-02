name = "Ramya S H"
print(name)
print(type(name))

# Lower method is used to convert the string to lowercase
print(name.lower())

# Upper method is used to convert the string to uppercase
print(name.upper())

# Title method is used to convert the string to titlecase
print(name.title())

para = "  this is a paragraph with multiple space  "
print(para)

# Strip method is used to remove all the whitespaces from the string
print(para.strip())

# lstrip method is used to remove all the whitespaces from the starting of the string
print(para.lstrip())

# rstrip method is used to remove all the whitespaces from the ending of the string
print(para.rstrip())

name = "Ramya S H"

# Replace method is used to replace the word from the string
print(name.replace("S H", "Kavya"))
# Replecing the original string
print(name.replace("Ramya", "Gowda"))
print(name)
# But here just we are printing the repleced string instead of replacing the original of the string
print(name.replace("Ramya","SH"))

fruits = "Apple, Mango, Jacfruit, Orange"
print(fruits)
#split method is used to split the string into multiple list items with a seperator
print(fruits.split(", "))
print(type(fruits.split(",")))

students = "'Akash', 'vikas', 'Adarsh', 'Guru' "
students = students.split("', ")
print("--------------------------------")
print(students)
print(type(students))
students = str(students)  # typecated the list to sring
print(type(students))
students = students.replace("'", "")
print(students)

sentence = "This is a first line. This is a second line. This is a third line"
print(sentence)
sentence = sentence.split(". ")
print(sentence)

# join method is used to combine the multiple  list items into single sting
print(" ".join(sentence))

# find method is used to get the index of the respective keyword
name = "Deepthi Anand"
print(name.find("Anand"))
print(name.find("a"))

# startswith method is used to check wheater the given string starts with a given value
print(name.startswith("Deepthi"))
print(name.startswith("Ullas"))

# endswith method is used to check wheater the given string starts with a given value
print(name.endswith("Anand"))
print(name.endswith("Ullas"))

word = "ABCD123"
print("-----------------")
print(word.isalpha()) # Cheks wheteh the given string contains only alphabet
print(word.isnumeric()) # checks whether the given string contains only numbers
print(word.isalnum()) # checks whesther the given string contains alphabets and numbers