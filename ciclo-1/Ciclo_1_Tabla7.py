"""
Imprime la tabla del 7, del 1 al 10, con este formato:

7 x 1 = 7
7 x 2 = 14
.....
"""

print("Esta es la tabla del 7 (1-10)")
print()

for i in range(1,11):
    x = 7 * i
    print("7 X", i , "=", x)