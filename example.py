# --------------------------------------- Variables

from math import fabs


is_game_over = False # Boolean
user_name = "John" # String
is_game_over = True
user_name = 5 # Int
percent_health = 0.5 # Float

print(user_name)

print(type(user_name))

# ------------------------------------------- Type Conversion 

str(percent_health) # convert to string 
int(is_game_over)
float(user_name)
bool(user_name)
user_name = ''
print(bool(user_name)) # if empty false 

# print(int("asdfasdf")) # Error

# ------------------------------------------- Operators

## Arithmetic

health = 20
print(health)
health += 10
print(health)


print(health % 2)
print(health // 2) # /
print(health ** 2) # *

first_name = "Devboi"
last_name = "Designs"
print(first_name + ' ' + last_name)

health += 20
health -= 20

name = 'Devboi'
name += ' Designs'

print(name)

## Comparison

# not
is_game_over = False
is_game_over = not is_game_over # True 
print(is_game_over)

# and
health = 0
lives = 0
print(health <= 0 and lives <= 0)

# or
print(health <= 0 or lives <= 0)


# ------------------------------------------- Collections

# List
inventory = ['Sword', 'Bread', 'Boots']
inventory[0] # Sword
inventory[1] = 'Apples'
print(inventory)

print(len(inventory)) # count/ length of 
print(max(inventory)) # item with highest value  
print(min(inventory)) # item with lowest value 

inventory.append('Hat') # Adds to end
inventory.insert(0, 'Knife') # insert at index
inventory.pop() # remove last item
inventory.remove('Sword') # remove particular item
inventory.clear() # empty list

print(inventory)


# 2D List

universe = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]

ninth_world = universe[2][1] # 8 
print(ninth_world)

universe.append([13, 14, 15])
universe[1].append(7)
universe[0].pop()
print(universe)

# Tuples

item = ('Health Kit', 4)
name = item[0]
print(name)
# item[1] = 10 # Error : can not re assign 
item = ("Knife", 1)
print(item)

print(item.count('Knife'))
print(item.index(1))

# Dictionaries
print('--------- Dictionaries')

inventory = {'Knife':1, 'Health Kit': 3, 'Wood': 5}

print(inventory['Health Kit']) # 3
inventory['Knife'] = 2
print(inventory)

inventory['Gold'] = 50 # will add key if doesnt excist {'Knife': 2, 'Health Kit': 3, 'Wood': 5, 'Gold': 50}
print(inventory)

print(inventory.get('Tim')) # none
print(inventory.get('Knife')) # 2 value

print(inventory.keys()) # dict_keys(['Knife', 'Health Kit', 'Wood', 'Gold'])
print(inventory.values()) # dict_values([2, 3, 5, 50])

popped_item = inventory.pop('Knife') # removes item
print(popped_item) # 2 value

# Ranges
print('--------- Ranges')

first_ten = range(10)
print(first_ten[0]) # 0
print(first_ten[9]) # 9

first_ten = range(1, 11)
print(first_ten[0]) # 1
print(first_ten[9]) # 10

reversed_ten = reversed(first_ten) # reverse list
reversed_ten = list(reversed_ten) # convert to list
print(reversed_ten) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(5 in first_ten) # will check if in range : True
print(5 not in first_ten) # will check if in range : True

# ----------- (start, stop, step)
print(list(range(1, 11, 2))) # will skip (2) every other one (odd)
print(list(range(0, 10, 2))) # will skip (2) every other one (even)
 