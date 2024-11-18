# cases
'''
In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ 
names when those names comprise multiple words, whereby the first letter of the first word is 
lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable 
for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), 
with all letters in lowercase. For instance, those same variables would be called name, first_name, 
and preferred_first_name, respectively, in Python.

In a file called cases.py, implement a function called camel2snake() that takes the name of a 
variable in camel case and outputs the corresponding name in snake case. 
Assume that the user’s input will indeed be in camel case.
'''


'''
Now make one that does the opposite: snake2camel()
'''


def camel2snake(name):
  
  snake_case = []
  for letters in name:
    if letters.isupper():
      snake_case.append("_")
    snake_case.append(letters.lower())
  return "".join(snake_case)

print(camel2snake("myName"))


def snake2camel(name):
 
  camel_case = name[0].upper()
  for letters in name[1:]:
    if letters == "_":
      camel_case += letters.upper()
    else:
      camel_case += letters
  return camel_case

print(snake2camel("myname")) 
