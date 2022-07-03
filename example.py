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
 

 # -------------------------------------------------------- Control Flow

 ## If Statements
print('---------------- If Statements')

key_press = 'd'
if key_press == 'r':
  print('Move right') # indent if statmetns
elif key_press == 'l':
  print('Move left')
else: 
  print('Invalid key')


## Ternary 

result = 'Move right' if key_press == 'r' else 'Move left'
print(result)

## Variants

num_lives = 3
health = 0
if health <= 0 and num_lives <= 0:
  # num_lives -= 1
  # print('You lost a life!')
  if num_lives <= 0:
    print('You died!')
elif health <= 10:
  print('Warning: less than 10% health')
elif health <= 50:
  print('Warning: less than 50% health')
else: 
  print('Great!')



# -------------------------------------------------------- Loops
print('------------- Loops')
 ## while

x_pos = 0
y_pos = 2
end_pos = 5
enemy_pos = 3
while x_pos < end_pos:
  x_pos += 1 
  print(x_pos)
  if y_pos > 1:
    continue # will skip next if statement/ and contiue with iteration 
  if x_pos == enemy_pos:
    print("You collided with enemy")
    break # will completely break out of loop
print('Game Over')  

## for
print('-------------for Loops')

our_range = range(1, 6)
for i in our_range:
  print(i) # 1 2 3 4 5 

inventory = ['Boots', 'Arrows', 'Bow', 'Sword']
for item in inventory:
  print(item)
  if item == 'Bow':
    break


# convert for to while
i = 0
while i < len(inventory):
  print(inventory[i])
  i += 1


# -------------------------------------------------------- Functions
print('------------- Functions')

def name():
  print('Code')

x_pos = 0
def move():
  global x_pos # must assign global to get access to global variables 
  x_pos += 1
  print(x_pos)

move()

# default value 
def dynamicMove(amount = 1):
  global x_pos
  x_pos += amount
  print(x_pos)

dynamicMove(5)
dynamicMove(10)
dynamicMove()

start_pos = 0
end_pos = 10
x_pos = 0

def moveAgain(x_pos, amount = 1):
  global start_pos, end_pos
  x_pos += amount
  print('this is the x_pos: ' + str(x_pos)) # this is the x_pos: 11 (20)
  if x_pos < start_pos:
    return start_pos
  elif x_pos > end_pos:
    return end_pos
  return x_pos # else is not needed because return will break from loop if condition is meet 
  

result = moveAgain(10) # 11
print(result) # 11

result = moveAgain(100, 10) # 20
print(result) # 20