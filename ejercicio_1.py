
# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

string = "esto es un ejercicio de python"
number = 8
lista = [1,2,3,4,5, "hola"]
es_miercoles = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

string_two = string[0:3]
print(string_two)
 
# Exercise 3: Use an index to grab the first element from your list.

print(lista[0])

# Exercise 4: Create a new number variable that adds 10 to your original number.

number_two = number + 10
print(number_two)

# Exercise 5: Use an index to get the last element in your list.

print(lista[5])

# Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
lista_de_nombres = names.split(',')
print(lista_de_nombres)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

string_three = string[0:4]
print(string_three.upper())

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

mensaje_error = f'ERROR: Has introducido la contraseña erróneamente {number} veces.'
print(mensaje_error)

# Exercise 9: Print “hello world”.

print("hello world")