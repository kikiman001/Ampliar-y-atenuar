import math

# Obtener el valor de pi
pi_value = math.pi

# Separar el valor entero y decimal de pi
integer_part = int(pi_value)
decimal_part = pi_value - integer_part

# Convertir el valor entero y decimal en su representación binaria
integer_part_bin = bin(integer_part)[2:]  # Ignorar el prefijo '0b'
decimal_part_bin = bin(int(decimal_part * (2**32)))[2:]  # Multiplicar por 2^32 para obtener la parte decimal en binario

# Imprimir la representación en bits del valor entero y decimal de pi
print("Representación en bits del valor entero de pi:", integer_part_bin)
print("Representación en bits del valor decimal de pi:", decimal_part_bin)

