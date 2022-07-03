# Python 101

- no brackets, indentation instead
- weak & dynamically typed
- very flexible but slightly slower runtime
- code is executed line by line, not all at once
- expressive, easy to learn

## Download

- [Python](https://www.python.org/downloads/)
- `brew install python`

# Variables

- Example

```py
is_game_over = False # Boolean
user_name = "John" # String
is_game_over = True
user_name = 5 # Int
percent_health = 0.5 # Float

print(user_name)

print(type(user_name))
```

# Type Conversion

- Example

```py
str(percent_health) # convert to string
int(is_game_over) # convert to int
float(user_name) # convert to float
bool(user_name) # convert to bool
user_name = ''
print(bool(user_name)) # if empty false

print(int("asdfasdf")) # Error
```

# Operators

## Arithmetic

```py
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
```

## Comparison

- Example

## Logical

- `>`
- `>=`
- `<`
- `<=`
- `==`
- `!=`
- `not` : reverses boolean
- `and` : same as &&
- `or` : same as ||

* Example

```py
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
```

# Collections

## Lists

- Example

```py
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
```

### 2D Lists

- Example

```py
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
```

## Tuples

- Example

```py

```
