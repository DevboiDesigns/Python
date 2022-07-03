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
