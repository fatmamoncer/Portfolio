#Comments
A comment is a piece of text within a program that is not executed. It can be used to provide additional information to aid in understanding the code.

The # character is used to start a comment and it continues until the end of the line
# Comment on a single line
 
user = "JDoe" # Comment after code
# elif Statement
 
pet_type = "fish"
 
if pet_type == "dog":
  print("You have a dog.")
elif pet_type == "cat":
  print("You have a cat.")
elif pet_type == "fish":
  # this is performed
  print("You have a fish")
else:
  print("Not sure!")


  #or statement
  
True or True      # Evaluates to True
True or False     # Evaluates to True
False or False    # Evaluates to False
1 < 2 or 3 < 1    # Evaluates to True
3 < 1 or 1 > 6    # Evaluates to False
1 == 1 or 1 < 2   # Evaluates to True




# Equal operator
if 'Yes' == 'Yes':
  # evaluates to True
  print('They are equal')
 
if (2 > 1) == (5 < 10):
  # evaluates to True
  print('Both expressions give the same result')
 
c = '2'
d = 2
 
if c == d:
  print('They are equal')
else:
  print('They are not equal')




  # Not Equals Operator
 
if "Yes" != "No":
  # evaluates to True
  print("They are NOT equal")
 
val1 = 10
val2 = 20
 
if val1 != val2:
  print("They are NOT equal")
 
if (10 > 1) != (10 > 1000):
  # True != False
  print("They are NOT equal")


  
a = 2
b = 3
a < b  # evaluates to True
a > b  # evaluates to False
a >= b # evaluates to False
a <= b # evaluates to True
a <= a # evaluates to True




# if Statement
test_value = 100
 
if test_value > 1:
  # Expression evaluates to True
  print("This code is executed!")
 
if test_value > 1000:
  # Expression evaluates to False
  print("This code is NOT executed!")
 
print("Program continues at this point.")



# else Statement
test_value = 50
 
if test_value < 1:
  print("Value is < 1")
else:
  print("Value is >= 1")
 
test_string = "VALID"
 
if test_string == "NOT_VALID":
  print("String equals NOT_VALID")
else:
  print("String equals something else!")


  
True and True     # Evaluates to True
True and False    # Evaluates to False
False and False   # Evaluates to False
1 == 1 and 1 < 2  # Evaluates to True
1 < 2 and 3 < 1   # Evaluates to False
"Yes" and 100     # Evaluates to Tru


is_true = True
is_false = False
 
print(type(is_true)) 
# will output: <class 'bool'>



not True     # Evaluates to False
not False    # Evaluates to True
1 > 2        # Evaluates to False
not 1 > 2    # Evaluates to True
1 == 1       # Evaluates to True
not 1 == 1   # Evaluates to False


primes = [2, 3, 5, 7, 11]
print(primes)
 
empty_list = []



items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']


numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]



orders = ['daisies', 'periwinkle']
orders.append('tulips')
print(orders)
# Result: ['daisies', 'periwinkle', 'tulips']




names = ['Roger', 'Rafael', 'Andy', 'Novak']

berries = ["blueberry", "cranberry", "raspberry"]
 
berries[0]   # "blueberry"
berries[2]   # "raspberry"


soups = ['minestrone', 'lentil', 'pho', 'laksa']
soups[-1]   # 'laksa'
soups[-3:]  # 'lentil', 'pho', 'laksa'
soups[:-2]  # 'minestrone', 'lentil



# 2D list of people's heights
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
# Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)
 
# Output
# 61




# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Removes the first occurance of "Chris"
shopping_line.remove("Chris")
print(shopping_line)
 
# Output
# ["Cole", "Kip", "Sylvana", "Chris"]



backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')
 
print(numPen)
# Output: 3



knapsack = [2, 4, 3, 7, 10]
size = len(knapsack)
print(size) 
# Output: 5

exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList)
# Output: [1, 2, 3, 4




tools = ['pen', 'hammer', 'lever']
tools_slice = tools[1:3] # ['hammer', 'lever']
tools_slice[0] = 'nail'
 
# Original list is unaltered:
print(tools) # ['pen', 'hammer', 'lever']



# Here is a list representing a line of people at a store
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
 
# Here is how to insert "Vikor" after "Maxium" and before "Martim"
store_line.insert(2, "Vikor")
 
print(store_line) 
# Output: ['Karla', 'Maxium', 'Vikor', 'Martim', 'Isabella']




cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
 
# Pop the last element
removed_element = cs_topics.pop()
 
print(cs_topics)
print(removed_element)
 
# Output:
# ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
# 'Clowns 101'
 
# Pop the element "Baloon Making"
cs_topics.pop(2)
print(cs_topics)
print(14%4)