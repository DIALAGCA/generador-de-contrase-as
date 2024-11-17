import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ñ{}()"

longitud = int(input('Dime la longitud de la contrasena(cuantos caracteres?)'))

new_password = ''

for i in range(longitud):

    new_password = new_password + random.choice(caracteres)
print("la contraseña generada es",new_password)

