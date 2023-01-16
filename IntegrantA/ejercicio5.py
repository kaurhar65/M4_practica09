# Lista con que la trabaja
areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]

# Accede a unas posiciones concretas i printa los valores correspondientes.
print(areas[1])
print(areas[13])
print(areas[5])
print(areas[:3])
print(areas[2:])
print(areas[9] + areas[11])

# Accede a la posición 7 para modificar su valor.
areas[7] = 75.0
print(areas)

# Con la función append añadimos dos valores más al final de la lista.
areas.append("Pati interior")
areas.append(2.78)
print(areas)
