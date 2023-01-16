# list areas a la que afegirem o canviarem dades
areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]
# impressió de parts de la llista, suma d'àrees i modificacions i afegiments a la llista:
print (areas[1])
print (areas[13])
print (areas[5])
print (areas[:3])
print (areas[2:])
print (areas[9]+areas[11])
areas[7]=12
print (areas)
areas.append("Pati interior")
areas.append(2.8)
print (areas)


